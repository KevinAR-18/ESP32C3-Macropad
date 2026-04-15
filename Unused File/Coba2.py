import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QLineEdit, QHBoxLayout, QVBoxLayout, QStackedLayout,
    QMessageBox, QCheckBox
)
from PySide6.QtCore import Qt


# ================= KEY CAPTURE LINEEDIT =================
class KeyCaptureEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Press shortcut...")
        self.setReadOnly(True)
        self.current_combo = []

    def keyPressEvent(self, event):
        keys = []

        if event.modifiers() & Qt.ControlModifier:
            keys.append("ctrl")
        if event.modifiers() & Qt.ShiftModifier:
            keys.append("shift")
        if event.modifiers() & Qt.AltModifier:
            keys.append("alt")

        key = event.key()
        if key not in (
            Qt.Key_Control, Qt.Key_Shift,
            Qt.Key_Alt, Qt.Key_Meta
        ):
            key_name = event.text().lower()
            if key_name:
                keys.append(key_name)

        self.current_combo = keys
        self.setText(" + ".join(keys))


# ================= MAIN WINDOW =================
class MacroPadGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ESP32C3 MacroPad")
        self.setFixedSize(700, 300)

        self.profile_index = 0
        self.profile_data = [{} for _ in range(5)]

        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)

        # ---------- TOP BAR ----------
        top_bar = QHBoxLayout()
        self.profile_buttons = []

        for i in range(5):
            btn = QPushButton(f"Profile {i+1}")
            btn.clicked.connect(lambda _, x=i: self.switch_profile(x))
            self.profile_buttons.append(btn)
            top_bar.addWidget(btn)

        settings_btn = QPushButton("⚙")
        settings_btn.setFixedWidth(40)
        settings_btn.clicked.connect(self.show_settings)
        top_bar.addWidget(settings_btn)

        main_layout.addLayout(top_bar)

        # ---------- STACK ----------
        self.stack = QStackedLayout()
        main_layout.addLayout(self.stack)

        # ---------- PROFILE PAGE ----------
        self.profile_page = QWidget()
        profile_layout = QVBoxLayout(self.profile_page)

        self.key_edits = []
        buttons_layout = QHBoxLayout()

        for i in range(5):
            col = QVBoxLayout()
            label = QLabel(f"Button {i+1}")
            edit = KeyCaptureEdit()
            self.key_edits.append(edit)

            col.addWidget(label)
            col.addWidget(edit)
            buttons_layout.addLayout(col)

        profile_layout.addLayout(buttons_layout)

        save_btn = QPushButton("SAVE PROFILE")
        save_btn.clicked.connect(self.save_profile)
        profile_layout.addWidget(save_btn, alignment=Qt.AlignCenter)

        self.stack.addWidget(self.profile_page)

        # ---------- SETTINGS PAGE ----------
        self.settings_page = QWidget()
        settings_layout = QVBoxLayout(self.settings_page)

        self.auto_start_chk = QCheckBox("Auto start with Windows")
        self.auto_detect_chk = QCheckBox("Auto detect ESP32 (recommended)")
        self.auto_detect_chk.setChecked(True)

        settings_layout.addWidget(self.auto_start_chk)
        settings_layout.addWidget(self.auto_detect_chk)

        back_btn = QPushButton("Back")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        settings_layout.addWidget(back_btn)

        self.stack.addWidget(self.settings_page)

        self.stack.setCurrentIndex(0)

    # ---------- LOGIC ----------
    def switch_profile(self, index):
        self.save_profile(silent=True)
        self.profile_index = index

        data = self.profile_data[index]
        for i, edit in enumerate(self.key_edits):
            edit.setText(data.get(i, ""))

    def save_profile(self, silent=False):
        data = {}
        for i, edit in enumerate(self.key_edits):
            data[i] = edit.text()

        self.profile_data[self.profile_index] = data

        if not silent:
            QMessageBox.information(self, "Saved", f"Profile {self.profile_index+1} saved")


    def show_settings(self):
        self.stack.setCurrentIndex(1)


# ================= RUN =================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MacroPadGUI()
    win.show()
    sys.exit(app.exec())
