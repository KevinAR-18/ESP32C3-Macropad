import os
import re
import subprocess
import sys
from importlib import import_module
from functools import partial
from pathlib import Path

from PySide6.QtCore import QEvent, QObject, Qt, QTimer, Signal
from PySide6.QtGui import QAction, QCursor, QFontMetrics, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QMainWindow,
    QMenu,
    QPushButton,
    QSystemTrayIcon,
    QVBoxLayout,
    QWidget,
)
from connection.manager import ConnectionManager
from connection.dialog import ConnectionDialog

from utils.date_utils import Date
from input.key_capture import KeyCaptureFilter
from input.shortcut_utils import (
    format_shortcut_display,
    global_event_to_shortcut_text,
    normalize_shortcut,
)
from config.settings_manager import (
    APPLICATION_MODE,
    SHORTCUT_MODE,
    apply_profile_mappings,
    apply_profile_titles,
    collect_profile_mappings,
    collect_profile_names,
    load_settings,
    save_settings,
    set_autostart,
    settings_path,
)
from ui.ui_functions import UIFunctions
from ui.ui_keybloom import Ui_MainWindow
from ui.preview_button import APP_MODE, KEYBOARD_MODE, UNSET_MODE, TransparentKeycapPreview

APP_NAME = "KeyBloom"
APP_VERSION = "1.1.0"
APP_ICON_FILE = "icon.ico"
START_MINIMIZED_ARG = "--start-minimized"
PROFILE_IDS = tuple(str(index) for index in range(1, 6))
PROFILE_LINE_COUNT = 6
SETTINGS_SAVE_DEBOUNCE_MS = 250
SPOTIFY_MODE_SESSION = "session"
SPOTIFY_WEB_STEP_PERCENT = 3

PROFILE_INPUT_STYLE = (
    "\nQLineEdit:hover { border: 2px solid #6f5fa8; background-color: rgba(255, 255, 255, 1); }"
    "\nQLineEdit:focus { border: 2px solid #584c90; background-color: rgba(255, 255, 255, 1); }"
)
PREVIEW_TOOLTIP = {
    SHORTCUT_MODE: "Klik kotak atas lalu pilih Shortcut Keyboard untuk merekam 5 detik.",
    APPLICATION_MODE: "Klik preview untuk pilih atau ganti aplikasi.",
}
CAPTURE_WINDOW_MS = 5000
SHORTCUT_PRESETS = [
    ("Alt+Tab", "Alt+Tab"),
    ("Win+Left", "Win+Left"),
    ("Win+Right", "Win+Right"),
    ("Win+Up", "Win+Up"),
    ("Win+Down", "Win+Down"),
    ("Ctrl+Win+Left", "Ctrl+Win+Left"),
    ("Ctrl+Win+Right", "Ctrl+Win+Right"),
]


def app_icon():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        icon_path = Path(sys._MEIPASS) / APP_ICON_FILE
    else:
        icon_path = Path(__file__).with_name(APP_ICON_FILE)
    if icon_path.is_file():
        return QIcon(str(icon_path))
    return QIcon(":/icon/images/icon_minimize.png")


class _PreviewClickFilter(QObject):
    def __init__(self, callback, parent=None):
        super().__init__(parent)
        self._callback = callback

    def eventFilter(self, obj, event):
        if isinstance(obj, QWidget) and event.type() == QEvent.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                self._callback(obj)
                return True
        return super().eventFilter(obj, event)


class MainWindow(QMainWindow):
    global_shortcut_captured = Signal(str)

    def __init__(self, start_minimized: bool = False):
        super().__init__()
        self._start_minimized = start_minimized
        if self._start_minimized:
            # Prevent a visible startup flash when Windows launches the app
            # from autostart.
            self.setAttribute(Qt.WA_DontShowOnScreen, True)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(app_icon())
        self.ui.version.setText(f"v{APP_VERSION}")

        self._loading_settings = False
        self._settings_initialized = False
        self._date_helper = Date()
        self._key_filter = KeyCaptureFilter(self)
        self._preview_filter = _PreviewClickFilter(self._on_preview_clicked, self)
        self._active_capture_slot = None
        self._shortcut_capture_timer = QTimer(self)
        self._shortcut_capture_timer.setSingleShot(True)
        self._shortcut_capture_timer.timeout.connect(self._stop_shortcut_capture)
        self._settings_save_timer = QTimer(self)
        self._settings_save_timer.setSingleShot(True)
        self._settings_save_timer.timeout.connect(self._save_settings)
        self._connection_settings = {}
        self._current_profile_id = "1"
        self._spotify_volume = None
        self._keyboard = None
        self._keyboard_capture_hook = None
        self._pycaw_interfaces = None
        self._psutil = None
        self.global_shortcut_captured.connect(self._apply_global_shortcut_capture)

        self._profile_name_inputs = self._build_profile_name_inputs()
        self._profile_title_labels = self._build_profile_title_labels()
        self._profile_pages = self._build_profile_pages()
        self._profile_buttons = self._build_profile_buttons()
        self._save_buttons = self._build_save_buttons()
        self._profile_slots = self._build_profile_slots()

        # Keep startup cheap, then lazily prepare profile widgets when the user
        # opens a page that actually needs them.
        self._configure_window()
        self._configure_settings_controls()
        self._setup_tray()
        self._show_page(self._profile_pages["1"], profile_id="1")
        self._connect_signals()
        self._setup_clock()
        self._load_settings()
        self._ensure_profile_slots_ready(self._current_profile_id)
        self._start_connections()
        if self._start_minimized:
            self.start_in_tray()

    def _configure_window(self):
        UIFunctions.set_borderless(self)
        UIFunctions.apply_border(self.ui.bgApp)
        UIFunctions.enable_drag(self, self.ui.titleFrame)

    def _setup_tray(self):
        self.tray = QSystemTrayIcon(self.windowIcon(), self)
        self.tray.setToolTip(APP_NAME)

        tray_menu = QMenu(self)
        show_action = QAction("Show", self)
        tray_menu.addSeparator()
        exit_action = QAction("Exit", self)

        show_action.triggered.connect(self.show_normal_from_tray)
        exit_action.triggered.connect(QApplication.quit)

        tray_menu.addAction(show_action)
        tray_menu.addAction(exit_action)
        self.tray.setContextMenu(tray_menu)
        self.tray.activated.connect(self._on_tray_activated)
        self.tray.show()

    def _connect_signals(self):
        self.ui.minimizeAppBtn.clicked.connect(self.minimize_to_tray)
        self.ui.closeAppBtn.clicked.connect(QApplication.quit)
        self.ui.btn_setting.clicked.connect(
            partial(self._show_page, self.ui.pageSettings)
        )
        self.ui.btn_savesettings.clicked.connect(self._save_settings)
        self.ui.cbAutostartup.toggled.connect(self._on_autostart_toggled)
        self.ui.cbAutodetect.toggled.connect(self._on_serial_settings_changed)
        self.ui.inputCOM.textChanged.connect(self._on_serial_settings_changed)

        for profile_id, button in self._profile_buttons.items():
            button.clicked.connect(
                partial(self._show_page, self._profile_pages[profile_id], profile_id=profile_id)
            )

        for button in self._save_buttons:
            button.clicked.connect(self._save_settings)

        for line_edit in self._profile_name_inputs:
            line_edit.textChanged.connect(self._schedule_save_settings)

    def _setup_clock(self):
        self._date_helper.update_time(self.ui.clockInfo)
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.start(1000)

    def _configure_settings_controls(self):
        self.ui.inputCOM.setPlaceholderText("Contoh: COM6")
        self.ui.inputCOM.setToolTip("Isi jika Auto Detect dimatikan.")
        self._remove_unused_spotify_ui()
        self._apply_settings_ui_state()

    def _remove_unused_spotify_ui(self):
        # These widgets exist in the generated UI but are not part of the
        # active flow, so they are detached to reduce idle memory usage.
        for attribute_name in ("frame_spotifyMode", "frame_spotifyApi"):
            frame = getattr(self.ui, attribute_name, None)
            if frame is None:
                continue
            frame.hide()
            layout = frame.parentWidget().layout() if frame.parentWidget() else None
            if layout is not None:
                layout.removeWidget(frame)
            frame.setParent(None)
            frame.deleteLater()
            setattr(self.ui, attribute_name, None)

    def _update_clock(self):
        self._date_helper.update_time(self.ui.clockInfo)

    def _build_profile_name_inputs(self):
        return [getattr(self.ui, f"customName{profile_id}") for profile_id in PROFILE_IDS]

    def _build_profile_title_labels(self):
        return [getattr(self.ui, f"titlepage{profile_id}") for profile_id in PROFILE_IDS]

    def _build_profile_pages(self):
        return {
            profile_id: getattr(self.ui, f"pageProfile{profile_id}")
            for profile_id in PROFILE_IDS
        }

    def _build_profile_buttons(self):
        return {
            profile_id: getattr(self.ui, f"btn_profile{profile_id}")
            for profile_id in PROFILE_IDS
        }

    def _build_save_buttons(self):
        return [getattr(self.ui, f"btn_saveload{profile_id}") for profile_id in PROFILE_IDS]

    def _build_profile_slots(self):
        profile_slots = {}
        slot_index = 1

        for profile_id in PROFILE_IDS:
            slots = []
            for line_number in range(1, PROFILE_LINE_COUNT + 1):
                slots.append(
                    {
                        "line_edit": getattr(self.ui, f"prof{profile_id}_line{line_number}"),
                        "preview_container": getattr(self.ui, f"slotPreview_{slot_index}"),
                        "slot_label": str(line_number),
                        "mode": SHORTCUT_MODE,
                        "stored_value": "",
                    }
                )
                slot_index += 1
            profile_slots[profile_id] = slots

        return profile_slots

    def _ensure_profile_slots_ready(self, profile_id):
        # Preview widgets are more expensive than plain line edits, so they are
        # created only for the currently visited profile page.
        slots = self._profile_slots.get(profile_id, [])
        for slot in slots:
            if slot.get("initialized"):
                continue
            self._setup_single_slot(slot)
            slot["initialized"] = True

    def _setup_single_slot(self, slot):
        line = slot["line_edit"]
        preview = self._build_preview_widget(slot)
        slot["preview_widget"] = preview
        slot["base_font_size"] = 10.0
        slot["base_stylesheet"] = line.styleSheet() + PROFILE_INPUT_STYLE

        line.setReadOnly(True)
        line.setProperty("capture_shortcut", False)
        line.installEventFilter(self._key_filter)
        line.setStyleSheet(slot["base_stylesheet"])
        line.textChanged.connect(partial(self._on_slot_text_changed, slot))

        preview.setCursor(QCursor(Qt.PointingHandCursor))
        preview.installEventFilter(self._preview_filter)

        self._apply_slot_mode(slot)

    def _build_preview_widget(self, slot):
        container = slot["preview_container"]
        layout = container.layout()
        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
        else:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        preview = TransparentKeycapPreview(slot["slot_label"], container)
        preview.setMinimumSize(container.minimumSize())
        preview.setMaximumSize(container.maximumSize())
        layout.addWidget(preview)
        return preview

    def _on_preview_clicked(self, preview_frame):
        slot = self._find_slot_by_preview(preview_frame)
        if slot is None:
            return
        self._show_slot_menu(slot)

    def _find_slot_by_preview(self, preview_frame):
        for slots in self._profile_slots.values():
            for slot in slots:
                if slot.get("preview_widget") is preview_frame:
                    return slot
        return None

    def _show_slot_menu(self, slot):
        menu = QMenu(self)
        keyboard_action = menu.addAction("Shortcut Keyboard")
        app_action = menu.addAction("Shortcut App")
        preset_menu = menu.addMenu("Preset Shortcut")
        preset_actions = {
            preset_menu.addAction(label): value for label, value in SHORTCUT_PRESETS
        }
        menu.addSeparator()
        clear_action = menu.addAction("Clear")

        preview = slot["preview_widget"]
        chosen_action = menu.exec(preview.mapToGlobal(preview.rect().center()))
        if chosen_action is keyboard_action:
            self._set_slot_mode(slot, SHORTCUT_MODE, arm_capture=True)
        elif chosen_action is app_action:
            self._set_slot_mode(slot, APPLICATION_MODE)
            self._browse_application(slot)
        elif chosen_action in preset_actions:
            self._apply_shortcut_preset(slot, preset_actions[chosen_action])
        elif chosen_action is clear_action:
            self._clear_slot(slot)

    def _set_slot_mode(self, slot, mode, arm_capture=False):
        previous_mode = slot.get("mode", SHORTCUT_MODE)
        if self._active_capture_slot is not None and self._active_capture_slot is not slot:
            self._stop_shortcut_capture()
        slot["mode"] = mode
        if mode == SHORTCUT_MODE and previous_mode == APPLICATION_MODE:
            slot["stored_value"] = ""
            slot["line_edit"].clear()
        elif mode == SHORTCUT_MODE:
            slot["stored_value"] = slot["line_edit"].text().strip()
        elif self._active_capture_slot is slot:
            self._stop_shortcut_capture()
        self._apply_slot_mode(slot)
        if mode == SHORTCUT_MODE and arm_capture:
            self._start_shortcut_capture(slot)
        self._schedule_save_settings()

    def _clear_slot(self, slot):
        if self._active_capture_slot is slot:
            self._stop_shortcut_capture()
        slot["mode"] = SHORTCUT_MODE
        slot["stored_value"] = ""
        slot["line_edit"].clear()
        self._apply_slot_mode(slot)
        self._schedule_save_settings()

    def _apply_slot_mode(self, slot):
        mode = slot.get("mode", SHORTCUT_MODE)
        line = slot["line_edit"]
        preview = slot.get("preview_widget")

        is_shortcut_mode = mode == SHORTCUT_MODE
        is_capture_active = is_shortcut_mode and self._active_capture_slot is slot
        line.setProperty("capture_shortcut", is_capture_active)
        line.setPlaceholderText(
            "Pilih Shortcut Keyboard untuk rekam 5 detik..."
            if is_shortcut_mode
            else "Nama aplikasi..."
        )

        preview_mode = UNSET_MODE
        if mode == APPLICATION_MODE:
            preview_mode = APP_MODE
        elif line.text().strip():
            preview_mode = KEYBOARD_MODE

        if preview is not None:
            preview.set_mode(preview_mode)
            preview.setToolTip(PREVIEW_TOOLTIP[mode])
        if is_capture_active:
            line.setToolTip("Rekam shortcut aktif selama 5 detik.")
        else:
            line.setToolTip(PREVIEW_TOOLTIP[mode])
        self._fit_line_edit_text(slot)

        if is_shortcut_mode:
            line.setReadOnly(True)
        else:
            self._apply_application_display(slot)

    def _apply_application_display(self, slot):
        stored_value = slot.get("stored_value", "").strip()
        line = slot["line_edit"]

        if not stored_value:
            line.clear()
            line.setToolTip("Klik kotak atas untuk memilih aplikasi atau shortcut file.")
            self._fit_line_edit_text(slot)
            return

        app_name = Path(stored_value).stem or Path(stored_value).name
        line.setText(app_name)
        line.setToolTip(stored_value)
        self._fit_line_edit_text(slot)

    def _browse_application(self, slot):
        current_value = slot.get("stored_value", "").strip()
        start_dir = os.path.dirname(current_value) if os.path.isfile(current_value) else ""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose Application",
            start_dir,
            "Applications (*.exe *.bat *.cmd *.lnk);;All Files (*)",
        )
        if file_path:
            slot["mode"] = APPLICATION_MODE
            slot["stored_value"] = file_path
            self._apply_slot_mode(slot)
            self._schedule_save_settings()

    def _apply_shortcut_preset(self, slot, shortcut_text: str):
        if self._active_capture_slot is slot:
            self._stop_shortcut_capture()
        slot["mode"] = SHORTCUT_MODE
        slot["stored_value"] = shortcut_text
        slot["line_edit"].setText(format_shortcut_display(shortcut_text))
        self._apply_slot_mode(slot)
        self._schedule_save_settings()

    def _start_shortcut_capture(self, slot):
        # Only one capture target should be active so the key event filter has
        # a single destination for the recorded shortcut.
        self._active_capture_slot = slot
        self._key_filter.reset()
        self._start_global_shortcut_capture()
        self._apply_slot_mode(slot)
        line = slot["line_edit"]
        line.setFocus()
        line.selectAll()
        self._shortcut_capture_timer.start(CAPTURE_WINDOW_MS)

    def _stop_shortcut_capture(self):
        if self._active_capture_slot is None:
            return

        slot = self._active_capture_slot
        self._active_capture_slot = None
        self._shortcut_capture_timer.stop()
        self._key_filter.reset()
        self._stop_global_shortcut_capture()
        self._apply_slot_mode(slot)

    def _start_global_shortcut_capture(self):
        keyboard_module = self._get_keyboard_module()
        if keyboard_module is None or self._keyboard_capture_hook is not None:
            return

        try:
            # Qt does not reliably receive media keys produced through Fn
            # layers, so a temporary global hook is used only during capture.
            self._keyboard_capture_hook = keyboard_module.hook(
                self._on_global_shortcut_event,
                suppress=False,
            )
        except Exception as error:
            print(f"[SHORTCUT] Global capture unavailable: {error}")
            self._keyboard_capture_hook = None

    def _stop_global_shortcut_capture(self):
        keyboard_module = self._get_keyboard_module()
        if keyboard_module is None or self._keyboard_capture_hook is None:
            self._keyboard_capture_hook = None
            return

        try:
            keyboard_module.unhook(self._keyboard_capture_hook)
        except Exception:
            pass
        self._keyboard_capture_hook = None

    def _on_global_shortcut_event(self, event):
        if self._active_capture_slot is None:
            return
        if getattr(event, "event_type", "") != "down":
            return

        shortcut_text = global_event_to_shortcut_text(getattr(event, "name", None))
        if not shortcut_text:
            return

        self.global_shortcut_captured.emit(shortcut_text)

    def _apply_global_shortcut_capture(self, shortcut_text: str):
        if self._active_capture_slot is None:
            return

        slot = self._active_capture_slot
        slot["mode"] = SHORTCUT_MODE
        slot["stored_value"] = shortcut_text
        line = slot["line_edit"]
        line.blockSignals(True)
        line.setText(format_shortcut_display(shortcut_text))
        line.blockSignals(False)
        self._fit_line_edit_text(slot)
        self._stop_shortcut_capture()
        self._schedule_save_settings()

    def _on_slot_text_changed(self, slot, *_args):
        if self._loading_settings:
            return
        if slot.get("mode") == SHORTCUT_MODE:
            slot["stored_value"] = slot["line_edit"].text().strip()
        self._fit_line_edit_text(slot)
        self._apply_slot_mode(slot)
        self._schedule_save_settings()

    def _fit_line_edit_text(self, slot):
        line = slot["line_edit"]
        text = line.text().strip()
        base_size = slot.get("base_font_size", 10.0)
        min_size = 5.0
        available_width = max(20, line.width() - 10)

        if not text:
            self._apply_line_font_size(slot, base_size)
            return

        size = base_size
        font = line.font()
        font.setPointSizeF(size)
        metrics = QFontMetrics(font)

        while size > min_size and metrics.horizontalAdvance(text) > available_width:
            size -= 0.5
            font.setPointSizeF(size)
            metrics = QFontMetrics(font)

        self._apply_line_font_size(slot, size)

    def _apply_line_font_size(self, slot, size):
        base_stylesheet = slot["base_stylesheet"]
        updated_stylesheet = re.sub(
            r"font-size:\s*[\d.]+pt;",
            f"font-size: {size:.1f}pt;",
            base_stylesheet,
            count=1,
        )
        slot["line_edit"].setStyleSheet(updated_stylesheet)

    def _serial_settings(self):
        return {
            "auto_detect": self.ui.cbAutodetect.isChecked(),
            "port": self.ui.inputCOM.text().strip(),
        }

    def _spotify_settings(self):
        return {"mode": SPOTIFY_MODE_SESSION}

    def _apply_settings_ui_state(self):
        self.ui.inputCOM.setEnabled(not self.ui.cbAutodetect.isChecked())

    def _on_serial_settings_changed(self, *_args):
        self._apply_settings_ui_state()
        if self._loading_settings:
            return
        if hasattr(self, "connections"):
            self.connections.worker.commands.put(("serial", self._serial_settings()))
        self._schedule_save_settings()

    def _load_settings(self):
        data = load_settings(settings_path())
        self._connection_settings = data.get("connection", {}) if data else {}
        if not data:
            self.ui.cbAutodetect.setChecked(True)
            self._apply_settings_ui_state()
            self._apply_profile_titles()
            self._show_page(self._profile_pages["1"], profile_id="1")
            self._settings_initialized = True
            return

        self._loading_settings = True
        try:
            # Many widget updates happen here; suppress autosave side effects
            # until the initial load sequence is finished.
            for line_edit, name in zip(
                self._profile_name_inputs, data.get("profile_names", [])
            ):
                line_edit.setText(name)

            self.ui.cbAutostartup.setChecked(bool(data.get("autostart", False)))
            serial_settings = data.get("serial", {})
            self.ui.cbAutodetect.setChecked(bool(serial_settings.get("auto_detect", True)))
            self.ui.inputCOM.setText(str(serial_settings.get("port", "")))
            self._apply_settings_ui_state()
            apply_profile_mappings(self._profile_slots, data.get("profiles", {}))
            # Always return to profile 1 when the app opens.
            self._show_page(self._profile_pages["1"], profile_id="1")
            self._refresh_slot_modes()
            self._apply_profile_titles()
            self._set_autostart(self.ui.cbAutostartup.isChecked())
        finally:
            self._loading_settings = False
            self._settings_initialized = True

    def _save_settings(self):
        self._settings_save_timer.stop()
        if self._loading_settings:
            return
        names = self._current_profile_names()
        self._apply_profile_titles(names)
        settings_data = {
            "profile_names": names,
            "autostart": self.ui.cbAutostartup.isChecked(),
            "active_profile": "1",
            "serial": self._serial_settings(),
            "connection": dict(self.connections.settings) if hasattr(self, "connections") else self._connection_settings,
            "spotify": self._spotify_settings(),
            "profiles": collect_profile_mappings(self._profile_slots),
        }
        # Persist into AppData so the packaged executable does not need write
        # permission inside its install directory.
        save_settings(settings_path(), settings_data)

    def _schedule_save_settings(self):
        if self._loading_settings:
            return
        self._settings_save_timer.start(SETTINGS_SAVE_DEBOUNCE_MS)

    def _current_profile_names(self):
        return collect_profile_names(self._profile_name_inputs)

    def _apply_profile_titles(self, names=None):
        apply_profile_titles(self._profile_title_labels, names or self._current_profile_names())

    def _refresh_slot_modes(self):
        for slots in self._profile_slots.values():
            for slot in slots:
                if slot.get("initialized"):
                    self._apply_slot_mode(slot)

    def _on_autostart_toggled(self, checked: bool):
        if self._loading_settings:
            return
        self._set_autostart(checked)
        self._schedule_save_settings()

    def _set_autostart(self, enabled: bool):
        if getattr(sys, "frozen", False):
            app_path = f'"{sys.executable}" {START_MINIMIZED_ARG}'
        else:
            app_path = (
                f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}" {START_MINIMIZED_ARG}'
            )

        set_autostart(enabled, APP_NAME, app_path)

    def _show_page(self, page, profile_id=None):
        if profile_id in self._profile_pages:
            self._current_profile_id = profile_id
            self._ensure_profile_slots_ready(profile_id)
        self.ui.stackedWidget.setCurrentWidget(page)
        if self._settings_initialized and not self._loading_settings:
            self._schedule_save_settings()

    def minimize_to_tray(self):
        self._hide_to_tray(show_message=True)

    def start_in_tray(self):
        self.hide()
        self.setAttribute(Qt.WA_DontShowOnScreen, False)

    def _hide_to_tray(self, show_message: bool):
        self.hide()
        if show_message:
            self.tray.showMessage(
                APP_NAME,
                "Application minimized to tray.",
                QSystemTrayIcon.Information,
                2000,
            )

    def show_normal_from_tray(self):
        self.show()
        self.raise_()
        self.activateWindow()

    def hideEvent(self, event):
        self.clock_timer.stop()
        super().hideEvent(event)

    def showEvent(self, event):
        if hasattr(self, "clock_timer") and not self.clock_timer.isActive():
            self._update_clock()
            self.clock_timer.start(1000)
        super().showEvent(event)

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show_normal_from_tray()

    def closeEvent(self, event):
        super().closeEvent(event)

    def _start_connections(self):
        self.connections = ConnectionManager(self._connection_settings, self._serial_settings(), self)
        self.connection_dialog = ConnectionDialog(self.connections, self)
        self.connections.event.connect(self._handle_device_event)
        self.connections.changed.connect(self._save_settings)
        self.connections.status.connect(lambda text: self.tray.setToolTip(f"{APP_NAME}: {text}"[:127]))
        self.connection_button = QPushButton("USB / Bluetooth Connection…", self)
        self.connection_button.setObjectName("connectionButton")
        self.connection_button.setCursor(Qt.PointingHandCursor)
        self.connection_button.setToolTip("Manage USB, Bluetooth devices, and power settings")
        self.connection_button.setStyleSheet("""
            QPushButton#connectionButton {
                background-color: #65518F;
                color: #FFFFFF;
                border: 2px solid #554278;
                border-radius: 8px;
                font: bold 10pt "Segoe UI";
                padding: 4px 10px;
            }
            QPushButton#connectionButton:hover {
                background-color: #7660A3;
                border-color: #65518F;
            }
            QPushButton#connectionButton:pressed {
                background-color: #4F3D73;
                border-color: #423260;
            }
            QPushButton#connectionButton:focus {
                border-color: #D9C9FF;
            }
            QPushButton#connectionButton:disabled {
                background-color: #DDD6E8;
                color: #62596F;
                border-color: #BEB3CE;
            }
        """)
        self.connection_button.clicked.connect(self.connection_dialog.show)
        self.ui.pageSettings.layout().addWidget(self.connection_button, 0, Qt.AlignHCenter)
        action = QAction("Connection…", self)
        action.triggered.connect(self.connection_dialog.show)
        self.tray.contextMenu().insertAction(self.tray.contextMenu().actions()[0], action)
        QApplication.instance().aboutToQuit.connect(self._stop_connections)
        self.connections.worker.start()

    def _stop_connections(self):
        self.connections.stop()
        self._save_settings()

    def _handle_device_event(self, event_text: str):
        # The firmware sends simple text commands; this is the translation layer
        # from hardware events into desktop actions.
        if event_text == "START":
            return

        button_match = re.fullmatch(r"BUTTON\s+(\d+)\s+PRESSED", event_text)
        if button_match:
            self._execute_profile_slot(int(button_match.group(1)))
            return

        if event_text == "ENC1 RIGHT":
            self._send_media_key("volume up")
            return
        if event_text == "ENC1 LEFT":
            self._send_media_key("volume down")
            return
        if event_text == "ENC1 BUTTON PRESSED":
            self._send_media_key("volume mute")
            return

        if event_text == "ENC2 RIGHT":
            self._adjust_spotify_volume(SPOTIFY_WEB_STEP_PERCENT / 100)
            return
        if event_text == "ENC2 LEFT":
            self._adjust_spotify_volume(-(SPOTIFY_WEB_STEP_PERCENT / 100))
            return
        if event_text == "ENC2 BUTTON PRESSED":
            self._send_media_key("play/pause media")

    def _execute_profile_slot(self, slot_number: int):
        slots = self._profile_slots.get(self._current_profile_id, [])
        slot_index = slot_number - 1
        if slot_index < 0 or slot_index >= len(slots):
            return

        slot = slots[slot_index]
        value = slot.get("stored_value", "").strip()
        if slot.get("mode") == APPLICATION_MODE:
            self._launch_application(value)
        else:
            self._send_shortcut(value)

    def _launch_application(self, target_path: str):
        if not target_path:
            return

        try:
            os.startfile(target_path)
        except AttributeError:
            subprocess.Popen([target_path])
        except OSError as error:
            print(f"[APP] Failed to open {target_path}: {error}")

    def _send_shortcut(self, shortcut_text: str):
        normalized = normalize_shortcut(shortcut_text)
        if not normalized:
            return

        keyboard_module = self._get_keyboard_module()
        if keyboard_module is None:
            return

        try:
            keyboard_module.press_and_release(normalized)
        except ValueError as error:
            print(f"[SHORTCUT] Invalid shortcut '{shortcut_text}': {error}")

    def _send_media_key(self, key_name: str):
        keyboard_module = self._get_keyboard_module()
        if keyboard_module is None:
            return

        try:
            keyboard_module.send(normalize_shortcut(key_name))
        except ValueError as error:
            print(f"[SHORTCUT] Invalid media key '{key_name}': {error}")

    def _adjust_spotify_volume(self, delta: float):
        spotify_volume = self._get_spotify_volume()
        if spotify_volume is None:
            print("[SPOTIFY] Spotify session not found.")
            return

        try:
            current_volume = spotify_volume.GetMasterVolume()
            spotify_volume.SetMasterVolume(min(max(current_volume + delta, 0.0), 1.0), None)
        except Exception:
            self._spotify_volume = None
            spotify_volume = self._get_spotify_volume()
            if spotify_volume is None:
                print("[SPOTIFY] Spotify session not found.")
                return
            current_volume = spotify_volume.GetMasterVolume()
            spotify_volume.SetMasterVolume(min(max(current_volume + delta, 0.0), 1.0), None)

    def _get_spotify_volume(self):
        pycaw_interfaces = self._get_pycaw_interfaces()
        if pycaw_interfaces is None:
            return None

        if not self._is_spotify_running():
            self._spotify_volume = None
            return None

        if self._spotify_volume is not None:
            return self._spotify_volume

        audio_utilities, simple_audio_volume = pycaw_interfaces
        for session in audio_utilities.GetAllSessions():
            process = session.Process
            if process and process.name().lower() == "spotify.exe":
                self._spotify_volume = session._ctl.QueryInterface(simple_audio_volume)
                return self._spotify_volume

        return None

    def _is_spotify_running(self) -> bool:
        psutil_module = self._get_psutil_module()
        if psutil_module is None:
            return False

        for process in psutil_module.process_iter(["name"]):
            try:
                if (process.info.get("name") or "").lower() == "spotify.exe":
                    return True
            except (psutil_module.NoSuchProcess, psutil_module.AccessDenied):
                continue
        return False

    def _get_keyboard_module(self):
        if self._keyboard is None:
            try:
                # Delay global hook modules until they are actually needed to
                # keep the tray process lighter at startup.
                self._keyboard = import_module("keyboard")
            except ImportError as error:
                print(f"[SHORTCUT] Keyboard module unavailable: {error}")
                return None
        return self._keyboard

    def _get_pycaw_interfaces(self):
        if self._pycaw_interfaces is None:
            try:
                pycaw_module = import_module("pycaw.pycaw")
            except ImportError as error:
                print(f"[SPOTIFY] Pycaw module unavailable: {error}")
                return None
            self._pycaw_interfaces = (
                pycaw_module.AudioUtilities,
                pycaw_module.ISimpleAudioVolume,
            )
        return self._pycaw_interfaces

    def _get_psutil_module(self):
        if self._psutil is None:
            try:
                self._psutil = import_module("psutil")
            except ImportError as error:
                print(f"[SPOTIFY] psutil module unavailable: {error}")
                return None
        return self._psutil


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName(APP_NAME)
    app.setApplicationDisplayName(APP_NAME)
    app.setWindowIcon(app_icon())
    start_minimized = START_MINIMIZED_ARG in sys.argv
    window = MainWindow(start_minimized=start_minimized)
    if not start_minimized:
        window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    

#Test Komentar
