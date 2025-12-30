import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QPushButton, QLineEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent


class KeyCaptureLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setPlaceholderText("Click here, then press shortcut...")
        self.setReadOnly(True)

    def keyPressEvent(self, event: QKeyEvent):
        keys = []

        # Modifier keys
        if event.modifiers() & Qt.ControlModifier:
            keys.append("Ctrl")
        if event.modifiers() & Qt.ShiftModifier:
            keys.append("Shift")
        if event.modifiers() & Qt.AltModifier:
            keys.append("Alt")

        key = event.key()

        # Ignore pure modifier press
        if key in (Qt.Key_Control, Qt.Key_Shift, Qt.Key_Alt):
            return

        # Clear shortcut
        if key == Qt.Key_Backspace:
            self.clear()
            return

        # Convert key to name
        key_name = Qt.Key(key).name.replace("Key_", "")
        keys.append(key_name)

        shortcut = "+".join(keys)
        self.setText(shortcut)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shortcut Capture Demo")
        self.setFixedSize(320, 180)

        layout = QVBoxLayout(self)  

        self.label = QLabel("Captured shortcut:")
        self.result_label = QLabel("-")
        self.result_label.setStyleSheet("font-weight: bold;")

        self.capture = KeyCaptureLineEdit()

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.save_shortcut)

        layout.addWidget(self.capture)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.label)
        layout.addWidget(self.result_label)

    def save_shortcut(self):
        text = self.capture.text().lower()
        self.result_label.setText(text)
        print(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
