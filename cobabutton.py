import sys

from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from preview_button import (
    APP_MODE,
    KEYBOARD_MODE,
    UNSET_MODE,
    TransparentKeycapPreview,
)


class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coba Button Preview")
        self.resize(760, 520)
        self.setStyleSheet(
            "QWidget { background: #F4F1FB; color: #2E2A44; font-family: 'Segoe UI'; }"
            "QFrame#panel { background: rgba(234, 228, 246, 0.92); border: 1px solid #D8D0EA; border-radius: 22px; }"
            "QPushButton { background: rgba(255, 255, 255, 0.72); border: 1px solid #CFC5E4; border-radius: 11px; padding: 8px 12px; font-weight: 600; }"
            "QPushButton:hover { background: rgba(255, 255, 255, 0.92); }"
        )

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(14)

        title = QLabel("Preview keycap transparan untuk slot macropad")
        title.setStyleSheet("font-size: 18px; font-weight: 700; color: #42356F;")
        layout.addWidget(title)

        subtitle = QLabel(
            "Widget preview sekarang dipisah ke file reusable sendiri. Di sini hanya demo host-nya."
        )
        subtitle.setWordWrap(True)
        subtitle.setStyleSheet("font-size: 11px; color: #5F557F;")
        layout.addWidget(subtitle)

        panel = QFrame()
        panel.setObjectName("panel")
        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(18)
        layout.addWidget(panel)

        grid = QGridLayout()
        grid.setHorizontalSpacing(18)
        grid.setVerticalSpacing(18)
        panel_layout.addLayout(grid)

        self.previews = [
            TransparentKeycapPreview("Slot Preview A"),
            TransparentKeycapPreview("Slot Preview B"),
            TransparentKeycapPreview("Slot Preview C"),
        ]
        self.previews[0].set_mode(UNSET_MODE)
        self.previews[1].set_mode(APP_MODE)
        self.previews[2].set_mode(KEYBOARD_MODE)

        for idx, preview in enumerate(self.previews):
            grid.addWidget(preview, 0, idx)

        controls = QHBoxLayout()
        controls.setSpacing(10)
        panel_layout.addLayout(controls)

        unset_button = QPushButton("Set Abu-Abu")
        unset_button.clicked.connect(lambda: self._set_all_modes(UNSET_MODE))
        controls.addWidget(unset_button)

        app_button = QPushButton("Set Shortcut App")
        app_button.clicked.connect(lambda: self._set_all_modes(APP_MODE))
        controls.addWidget(app_button)

        keyboard_button = QPushButton("Set Shortcut Keyboard")
        keyboard_button.clicked.connect(lambda: self._set_all_modes(KEYBOARD_MODE))
        controls.addWidget(keyboard_button)

        controls.addStretch(1)

    def _set_all_modes(self, mode: str):
        for preview in self.previews:
            preview.set_mode(mode)


def main():
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
