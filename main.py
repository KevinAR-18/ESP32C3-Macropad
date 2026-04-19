import os
import sys
from functools import partial

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QSystemTrayIcon

from date_utils import Date
from key_capture import KeyCaptureFilter
import resources_rc
from settings_manager import (
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

APP_NAME = "KeyBloom"
PROFILE_IDS = tuple(str(index) for index in range(1, 6))
PROFILE_LINE_COUNT = 6
PROFILE_INPUT_STYLE = (
    "\nQLineEdit:hover { border: 2px solid #6f5fa8; background-color: rgba(255, 255, 255, 1); }"
    "\nQLineEdit:focus { border: 2px solid #584c90; background-color: rgba(255, 255, 255, 1); }"
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._loading_settings = False
        self._date_helper = Date()
        self._key_filter = KeyCaptureFilter(self)

        self._profile_lines = self._build_profile_line_map()
        self._profile_name_inputs = self._build_profile_name_inputs()
        self._profile_title_labels = self._build_profile_title_labels()
        self._profile_pages = self._build_profile_pages()
        self._profile_buttons = self._build_profile_buttons()
        self._save_buttons = self._build_save_buttons()

        self._configure_window()
        self._setup_tray()
        self._setup_profile_inputs()
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
            button.clicked.connect(partial(self._show_page, self._profile_pages[profile_id]))

        for button in self._save_buttons:
            button.clicked.connect(self._save_settings)

    def _setup_clock(self):
        self._date_helper.update_time(self.ui.clockInfo)
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self._update_clock)
        self.clock_timer.start(1000)

    def _update_clock(self):
        self._date_helper.update_time(self.ui.clockInfo)

    def _build_profile_line_map(self):
        return {
            profile_id: [
                getattr(self.ui, f"prof{profile_id}_line{line_number}")
                for line_number in range(1, PROFILE_LINE_COUNT + 1)
            ]
            for profile_id in PROFILE_IDS
        }

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

    def _setup_profile_inputs(self):
        for lines in self._profile_lines.values():
            for line in lines:
                line.setReadOnly(True)
                line.installEventFilter(self._key_filter)
                line.setStyleSheet(line.styleSheet() + PROFILE_INPUT_STYLE)

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
            apply_profile_mappings(self._profile_lines, data.get("profiles", {}))
            self._apply_profile_titles()
            self._set_autostart(self.ui.cbAutostartup.isChecked())
        finally:
            self._loading_settings = False

    def _save_settings(self):
        names = self._current_profile_names()
        self._apply_profile_titles(names)
        save_settings(
            settings_path(),
            {
                "profile_names": names,
                "autostart": self.ui.cbAutostartup.isChecked(),
                "profiles": collect_profile_mappings(self._profile_lines),
            },
        )

    def _current_profile_names(self):
        return collect_profile_names(self._profile_name_inputs)

    def _apply_profile_titles(self, names=None):
        apply_profile_titles(self._profile_title_labels, names or self._current_profile_names())

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
