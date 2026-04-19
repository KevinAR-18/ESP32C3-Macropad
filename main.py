import os
import re
import sys
from functools import partial
from pathlib import Path

from PySide6.QtCore import QEvent, QObject, Qt, QTimer
from PySide6.QtGui import QAction, QCursor, QFontMetrics, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFrame,
    QMainWindow,
    QMenu,
    QSystemTrayIcon,
    QVBoxLayout,
    QWidget,
)

from date_utils import Date
from key_capture import KeyCaptureFilter
import resources_rc
from settings_manager import (
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
from ui_functions import UIFunctions
from ui_keybloom import Ui_MainWindow
from preview_button import APP_MODE, KEYBOARD_MODE, UNSET_MODE, TransparentKeycapPreview

APP_NAME = "KeyBloom"
PROFILE_IDS = tuple(str(index) for index in range(1, 6))
PROFILE_LINE_COUNT = 6

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
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._loading_settings = False
        self._date_helper = Date()
        self._key_filter = KeyCaptureFilter(self)
        self._preview_filter = _PreviewClickFilter(self._on_preview_clicked, self)
        self._active_capture_slot = None
        self._shortcut_capture_timer = QTimer(self)
        self._shortcut_capture_timer.setSingleShot(True)
        self._shortcut_capture_timer.timeout.connect(self._stop_shortcut_capture)

        self._profile_name_inputs = self._build_profile_name_inputs()
        self._profile_title_labels = self._build_profile_title_labels()
        self._profile_pages = self._build_profile_pages()
        self._profile_buttons = self._build_profile_buttons()
        self._save_buttons = self._build_save_buttons()
        self._profile_slots = self._build_profile_slots()

        self._configure_window()
        self._setup_tray()
        self._setup_profile_slots()
        self._show_page(self._profile_pages["1"])
        self._connect_signals()
        self._setup_clock()
        self._load_settings()

    def _configure_window(self):
        UIFunctions.set_borderless(self)
        UIFunctions.apply_border(self.ui.bgApp)
        UIFunctions.enable_drag(self, self.ui.titleFrame)

    def _setup_tray(self):
        self.tray = QSystemTrayIcon(QIcon(":/icon/images/icon_minimize.png"), self)
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

        for profile_id, button in self._profile_buttons.items():
            button.clicked.connect(
                partial(self._show_page, self._profile_pages[profile_id])
            )

        for button in self._save_buttons:
            button.clicked.connect(self._save_settings)

        for line_edit in self._profile_name_inputs:
            line_edit.textChanged.connect(self._save_settings)

    def _setup_clock(self):
        self._date_helper.update_time(self.ui.clockInfo)
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.start(1000)

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

    def _setup_profile_slots(self):
        for slots in self._profile_slots.values():
            for slot in slots:
                self._setup_single_slot(slot)

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
        self._save_settings()

    def _clear_slot(self, slot):
        if self._active_capture_slot is slot:
            self._stop_shortcut_capture()
        slot["mode"] = SHORTCUT_MODE
        slot["stored_value"] = ""
        slot["line_edit"].clear()
        self._apply_slot_mode(slot)
        self._save_settings()

    def _apply_slot_mode(self, slot):
        mode = slot.get("mode", SHORTCUT_MODE)
        line = slot["line_edit"]
        preview = slot["preview_widget"]

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
            self._save_settings()

    def _apply_shortcut_preset(self, slot, shortcut_text: str):
        if self._active_capture_slot is slot:
            self._stop_shortcut_capture()
        slot["mode"] = SHORTCUT_MODE
        slot["stored_value"] = shortcut_text
        slot["line_edit"].setText(shortcut_text)
        self._apply_slot_mode(slot)
        self._save_settings()

    def _start_shortcut_capture(self, slot):
        self._active_capture_slot = slot
        self._key_filter.reset()
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
        self._apply_slot_mode(slot)

    def _on_slot_text_changed(self, slot, *_args):
        if self._loading_settings:
            return
        if slot.get("mode") == SHORTCUT_MODE:
            slot["stored_value"] = slot["line_edit"].text().strip()
        self._fit_line_edit_text(slot)
        self._apply_slot_mode(slot)
        self._save_settings()

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

    def _load_settings(self):
        data = load_settings(settings_path())
        if not data:
            self._apply_profile_titles()
            return

        self._loading_settings = True
        try:
            for line_edit, name in zip(
                self._profile_name_inputs, data.get("profile_names", [])
            ):
                line_edit.setText(name)

            self.ui.cbAutostartup.setChecked(bool(data.get("autostart", False)))
            apply_profile_mappings(self._profile_slots, data.get("profiles", {}))
            self._refresh_slot_modes()
            self._apply_profile_titles()
            self._set_autostart(self.ui.cbAutostartup.isChecked())
        finally:
            self._loading_settings = False

    def _save_settings(self):
        if self._loading_settings:
            return
        names = self._current_profile_names()
        self._apply_profile_titles(names)
        save_settings(
            settings_path(),
            {
                "profile_names": names,
                "autostart": self.ui.cbAutostartup.isChecked(),
                "profiles": collect_profile_mappings(self._profile_slots),
            },
        )

    def _current_profile_names(self):
        return collect_profile_names(self._profile_name_inputs)

    def _apply_profile_titles(self, names=None):
        apply_profile_titles(self._profile_title_labels, names or self._current_profile_names())

    def _refresh_slot_modes(self):
        for slots in self._profile_slots.values():
            for slot in slots:
                self._apply_slot_mode(slot)

    def _on_autostart_toggled(self, checked: bool):
        if self._loading_settings:
            return
        self._set_autostart(checked)
        self._save_settings()

    def _set_autostart(self, enabled: bool):
        if getattr(sys, "frozen", False):
            app_path = sys.executable
        else:
            app_path = f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}"'

        set_autostart(enabled, APP_NAME, app_path)

    def _show_page(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def minimize_to_tray(self):
        self.hide()
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

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            self.show_normal_from_tray()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
