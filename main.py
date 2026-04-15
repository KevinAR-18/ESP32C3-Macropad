import json
import os
import sys
from PySide6.QtCore import QCoreApplication, QDateTime, QEvent, QObject, Qt, QTimer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QSystemTrayIcon,
)

try:
    import winreg
except ImportError:
    winreg = None

from ui_functions import UIFunctions
from ui_keybloom import Ui_MainWindow
import resources_rc

# Class untuk mengatur Hari dan Waktu
class Date:
    def update_time(self, label: QLabel):
        current_time = QDateTime.currentDateTime()

        time_text = current_time.toString("HH:mm")
        date_text = current_time.toString("dddd, dd MMMM yyyy")

        label.setText(QCoreApplication.translate("MainWindow", f"{time_text} - {date_text}", None))


class _KeyCaptureFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.active_keys = []

    def eventFilter(self, obj, event):
        if not isinstance(obj, QLineEdit):
            return super().eventFilter(obj, event)

        if event.type() == QEvent.KeyPress:
            key = event.key()

            if key in (Qt.Key_Backspace, Qt.Key_Delete):
                obj.clear()
                self.active_keys.clear()
                return True

            if key in (Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt):
                self._add_key(key)
                return True

            self._add_key(key)
            self._update_text(obj, event.modifiers())
            return True

        if event.type() == QEvent.KeyRelease:
            self._remove_key(event.key())
            return True

        return super().eventFilter(obj, event)

    def _add_key(self, key):
        if key not in self.active_keys:
            self.active_keys.append(key)

    def _remove_key(self, key):
        if key in self.active_keys:
            self.active_keys.remove(key)

    def _update_text(self, obj, modifiers):
        keys = []

        if (modifiers & Qt.ControlModifier) or (Qt.Key_Control in self.active_keys):
            keys.append("Ctrl")
        if (modifiers & Qt.ShiftModifier) or (Qt.Key_Shift in self.active_keys):
            keys.append("Shift")
        if (modifiers & Qt.AltModifier) or (Qt.Key_Alt in self.active_keys):
            keys.append("Alt")

        for key in self.active_keys:
            if key in (Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt):
                continue
            key_name = Qt.Key(key).name.replace("Key_", "")
            keys.append(key_name)

        if keys:
            obj.setText("+".join(keys))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._loading_settings = False
        UIFunctions.set_borderless(self)
        UIFunctions.apply_border(self.ui.bgApp)
        UIFunctions.enable_drag(self, self.ui.titleFrame)
        self._setup_tray()
        self._connect_buttons()
        self._setup_clock()
        self._setup_profile_inputs()
        self._setup_settings()

    def _setup_tray(self):
        tray_icon = QIcon(":/icon/images/icon_minimize.png")
        self.tray = QSystemTrayIcon(tray_icon, self)
        self.tray.setToolTip("KeyBloom")

        tray_menu = QMenu()
        show_action = QAction("Show", self)
        exit_action = QAction("Exit", self)

        show_action.triggered.connect(self.show_normal_from_tray)
        exit_action.triggered.connect(QApplication.quit)

        tray_menu.addAction(show_action)
        tray_menu.addSeparator()
        tray_menu.addAction(exit_action)

        self.tray.setContextMenu(tray_menu)
        self.tray.activated.connect(self._on_tray_activated)
        self.tray.show()

    def _connect_buttons(self):
        self.ui.minimizeAppBtn.clicked.connect(self.minimize_to_tray)
        self.ui.closeAppBtn.clicked.connect(QApplication.quit)

        self.ui.btn_profile1.clicked.connect(lambda: self._show_page(self.ui.pageProfile1))
        self.ui.btn_profile2.clicked.connect(lambda: self._show_page(self.ui.pageProfile2))
        self.ui.btn_profile3.clicked.connect(lambda: self._show_page(self.ui.pageProfile3))
        self.ui.btn_profile4.clicked.connect(lambda: self._show_page(self.ui.pageProfile4))
        self.ui.btn_profile5.clicked.connect(lambda: self._show_page(self.ui.pageProfile5))
        self.ui.btn_setting.clicked.connect(lambda: self._show_page(self.ui.pageSettings))

        self.ui.btn_savesettings.clicked.connect(self._save_settings)
        self.ui.cbAutostartup.toggled.connect(self._on_autostart_toggled)

        self.ui.btn_saveload1.clicked.connect(self._save_settings)
        self.ui.btn_saveload2.clicked.connect(self._save_settings)
        self.ui.btn_saveload3.clicked.connect(self._save_settings)
        self.ui.btn_saveload4.clicked.connect(self._save_settings)
        self.ui.btn_saveload5.clicked.connect(self._save_settings)

    def _setup_clock(self):
        self.date_helper = Date()
        self.date_helper.update_time(self.ui.clockInfo)
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(
            lambda: self.date_helper.update_time(self.ui.clockInfo)
        )
        self.clock_timer.start(1000)

    def _settings_path(self) -> str:
        if getattr(sys, "frozen", False):
            base_dir = os.path.dirname(sys.executable)
        else:
            base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        return os.path.join(base_dir, "settings.json")

    def _setup_profile_inputs(self):
        self._profile_lines = {
            "1": [
                self.ui.prof1_line1,
                self.ui.prof1_line2,
                self.ui.prof1_line3,
                self.ui.prof1_line4,
                self.ui.prof1_line5,
                self.ui.prof1_line6,
            ],
            "2": [
                self.ui.prof2_line1,
                self.ui.prof2_line2,
                self.ui.prof2_line3,
                self.ui.prof2_line4,
                self.ui.prof2_line5,
                self.ui.prof2_line6,
            ],
            "3": [
                self.ui.prof3_line1,
                self.ui.prof3_line2,
                self.ui.prof3_line3,
                self.ui.prof3_line4,
                self.ui.prof3_line5,
                self.ui.prof3_line6,
            ],
            "4": [
                self.ui.prof4_line1,
                self.ui.prof4_line2,
                self.ui.prof4_line3,
                self.ui.prof4_line4,
                self.ui.prof4_line5,
                self.ui.prof4_line6,
            ],
            "5": [
                self.ui.prof5_line1,
                self.ui.prof5_line2,
                self.ui.prof5_line3,
                self.ui.prof5_line4,
                self.ui.prof5_line5,
                self.ui.prof5_line6,
            ],
        }
        self._key_filter = _KeyCaptureFilter(self)
        for lines in self._profile_lines.values():
            for line in lines:
                line.setReadOnly(True)
                line.installEventFilter(self._key_filter)
                line.setStyleSheet(
                    line.styleSheet()
                    + "\nQLineEdit:hover { border: 2px solid #6f5fa8; background-color: rgba(255, 255, 255, 1); }"
                    + "\nQLineEdit:focus { border: 2px solid #584c90; background-color: rgba(255, 255, 255, 1); }"
                )

    def _get_profile_inputs(self):
        return [
            self.ui.customName1,
            self.ui.customName2,
            self.ui.customName3,
            self.ui.customName4,
            self.ui.customName5,
        ]

    def _apply_profile_titles(self, names):
        title_labels = [
            self.ui.titlepage1,
            self.ui.titlepage2,
            self.ui.titlepage3,
            self.ui.titlepage4,
            self.ui.titlepage5,
        ]
        for idx, label in enumerate(title_labels):
            label.setText(names[idx])

    def _setup_settings(self):
        self._load_settings()

    def _load_settings(self):
        path = self._settings_path()
        if not os.path.exists(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            names = data.get("profile_names", [])
            autostart = bool(data.get("autostart", False))
            profiles = data.get("profiles", {})
        except (OSError, json.JSONDecodeError):
            return

        self._loading_settings = True
        inputs = self._get_profile_inputs()
        for idx, line_edit in enumerate(inputs):
            if idx < len(names):
                line_edit.setText(names[idx])

        self.ui.cbAutostartup.setChecked(autostart)
        self._apply_profile_titles(self._current_profile_names())
        self._apply_profile_mappings(profiles)
        self._set_autostart(autostart)
        self._loading_settings = False

    def _current_profile_names(self):
        defaults = [
            "Custom Title #1",
            "Custom Title #2",
            "Custom Title #3",
            "Custom Title #4",
            "Custom Title #5",
        ]
        names = []
        for idx, line_edit in enumerate(self._get_profile_inputs()):
            text = line_edit.text().strip()
            names.append(text if text else defaults[idx])
        return names

    def _save_settings(self):
        names = self._current_profile_names()
        self._apply_profile_titles(names)
        data = {
            "profile_names": names,
            "autostart": self.ui.cbAutostartup.isChecked(),
            "profiles": self._profile_mappings(),
        }
        path = self._settings_path()
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def _profile_mappings(self):
        mappings = {}
        for profile, lines in self._profile_lines.items():
            mappings[profile] = [line.text().strip() for line in lines]
        return mappings

    def _apply_profile_mappings(self, mappings):
        for profile, lines in self._profile_lines.items():
            values = mappings.get(profile, [])
            for idx, line in enumerate(lines):
                if idx < len(values):
                    line.setText(values[idx])

    def _on_autostart_toggled(self, checked: bool):
        if self._loading_settings:
            return
        self._set_autostart(checked)
        self._save_settings()

    def _set_autostart(self, enabled: bool):
        if winreg is None:
            return
        app_name = "KeyBloom"
        run_key = r"Software\Microsoft\Windows\CurrentVersion\Run"

        if getattr(sys, "frozen", False):
            app_path = sys.executable
        else:
            app_path = f'"{sys.executable}" "{os.path.abspath(sys.argv[0])}"'

        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key, 0, winreg.KEY_SET_VALUE) as key:
                if enabled:
                    winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
                else:
                    try:
                        winreg.DeleteValue(key, app_name)
                    except FileNotFoundError:
                        pass
        except OSError:
            pass

    def _show_page(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def minimize_to_tray(self):
        self.hide()
        self.tray.showMessage(
            "KeyBloom",
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