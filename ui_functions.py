from PySide6.QtCore import QObject, QPoint, Qt, QEvent
from PySide6.QtWidgets import QMainWindow, QWidget


class _DragFilter(QObject):
    def __init__(self, window: QMainWindow):
        super().__init__(window)
        self.window = window
        self.drag_pos: QPoint | None = None

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()
            return True

        if event.type() == QEvent.MouseMove and self.drag_pos:
            if event.buttons() == Qt.LeftButton:
                delta = event.globalPosition().toPoint() - self.drag_pos
                self.window.move(self.window.pos() + delta)
                self.drag_pos = event.globalPosition().toPoint()
                return True

        if event.type() == QEvent.MouseButtonRelease:
            self.drag_pos = None
            return True

        return super().eventFilter(obj, event)


class UIFunctions:
    @staticmethod
    def set_borderless(window: QMainWindow) -> None:
        window.setWindowFlags(
            Qt.FramelessWindowHint | Qt.Window | Qt.CustomizeWindowHint
        )
        window.setAttribute(Qt.WA_TranslucentBackground, True)
        window.setWindowFlag(Qt.WindowSystemMenuHint, False)
        window.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        window.setWindowFlag(Qt.WindowCloseButtonHint, False)

    @staticmethod
    def apply_border(
        widget: QWidget, color: str = "#b9aedc", radius: int = 12
    ) -> None:
        widget.setStyleSheet(
            widget.styleSheet()
            + f"\n#bgApp {{ border: 1px solid {color}; border-radius: {radius}px; }}"
        )

    @staticmethod
    def enable_drag(window: QMainWindow, drag_widget: QWidget) -> None:
        drag_filter = _DragFilter(window)
        drag_widget.installEventFilter(drag_filter)
        window._drag_filter = drag_filter
