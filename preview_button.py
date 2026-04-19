from __future__ import annotations

from PySide6.QtCore import Property, QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup, Qt
from PySide6.QtGui import QColor, QFont, QPainter, QPainterPath, QPen
from PySide6.QtWidgets import QSizePolicy, QWidget

UNSET_MODE = "unset"
APP_MODE = "application"
KEYBOARD_MODE = "keyboard"
DEFAULT_SLOT_BODY_COLORS = {
    1: "#D0C5E3",
    2: "#F2C9D3",
    3: "#E88C8D",
    4: "#9ED1D3",
    5: "#E3E7AA",
    6: "#C9E0B6",
}
DEFAULT_SLOT_TEXT_COLOR = "#111111"

MODE_COLORS = {
    UNSET_MODE: {
        "legend": QColor(255, 255, 255, 205),
        "body": QColor(255, 255, 255, 170),
        "surface": QColor(255, 255, 255, 115),
        "rim": QColor(255, 255, 255, 185),
    },
    APP_MODE: {
        "legend": QColor(255, 255, 255, 205),
        "body": QColor(255, 255, 255, 170),
        "surface": QColor(255, 255, 255, 115),
        "rim": QColor(255, 255, 255, 185),
    },
    KEYBOARD_MODE: {
        "legend": QColor(255, 255, 255, 205),
        "body": QColor(255, 255, 255, 170),
        "surface": QColor(255, 255, 255, 115),
        "rim": QColor(255, 255, 255, 185),
    },
}

MODE_TITLES = {
    UNSET_MODE: "Unassigned",
    APP_MODE: "Shortcut App",
    KEYBOARD_MODE: "Shortcut Keyboard",
}


class TransparentKeycapPreview(QWidget):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self._title = title
        self._mode = UNSET_MODE
        self._press_depth = 0.0
        self._glow_strength = 0.0

        self.setMinimumSize(115, 130)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCursor(Qt.PointingHandCursor)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self._press_down = QPropertyAnimation(self, b"pressDepth", self)
        self._press_down.setDuration(90)
        self._press_down.setStartValue(0.0)
        self._press_down.setEndValue(1.0)
        self._press_down.setEasingCurve(QEasingCurve.OutCubic)

        self._press_up = QPropertyAnimation(self, b"pressDepth", self)
        self._press_up.setDuration(150)
        self._press_up.setStartValue(1.0)
        self._press_up.setEndValue(0.0)
        self._press_up.setEasingCurve(QEasingCurve.OutBack)

        self._press_anim = QSequentialAnimationGroup(self)
        self._press_anim.addAnimation(self._press_down)
        self._press_anim.addAnimation(self._press_up)

        self._glow_anim = QPropertyAnimation(self, b"glowStrength", self)
        self._glow_anim.setDuration(220)
        self._glow_anim.setStartValue(0.15)
        self._glow_anim.setEndValue(1.0)
        self._glow_anim.setEasingCurve(QEasingCurve.OutCubic)

    def get_press_depth(self):
        return self._press_depth

    def set_press_depth(self, value):
        self._press_depth = float(value)
        self.update()

    pressDepth = Property(float, get_press_depth, set_press_depth)

    def get_glow_strength(self):
        return self._glow_strength

    def set_glow_strength(self, value):
        self._glow_strength = float(value)
        self.update()

    glowStrength = Property(float, get_glow_strength, set_glow_strength)

    def set_mode(self, mode: str):
        self._mode = mode
        self._glow_anim.stop()
        self._glow_anim.setStartValue(self._glow_strength)
        self._glow_anim.setEndValue(0.15 if mode == UNSET_MODE else 1.0)
        self._glow_anim.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._press_anim.stop()
            self._press_anim.start()
        super().mousePressEvent(event)

    def paintEvent(self, event):
        del event
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        colors = MODE_COLORS[self._mode]
        slot_number = int(self._title)
        body_color = QColor(DEFAULT_SLOT_BODY_COLORS.get(slot_number, "#FFFFFF"))
        legend_color = QColor(colors["legend"])
        outer_rect = self.rect().adjusted(6, 6, -6, -6)
        key_rect = outer_rect.adjusted(10, 10, -10, -18)
        press_offset = 2 * self._press_depth
        key_rect = key_rect.translated(0, press_offset)

        glow_rect = key_rect.adjusted(-10, -10, 10, 10)
        glow_color = QColor(body_color)
        glow_color.setAlpha(int(22 + 80 * self._glow_strength))
        painter.setBrush(glow_color)
        painter.drawRoundedRect(glow_rect, 24, 24)

        shadow = QColor(40, 44, 60, 28)
        painter.setBrush(shadow)
        painter.drawRoundedRect(key_rect.translated(0, 4), 18, 18)

        painter.setBrush(body_color)
        painter.drawRoundedRect(key_rect, 16, 16)

        inner_surface = key_rect.adjusted(6, 6, -6, -6)
        surface_color = QColor(body_color)
        surface_color.setAlpha(min(255, body_color.alpha() + 18))
        painter.setBrush(surface_color)
        painter.drawRoundedRect(inner_surface, 12, 12)

        accent_rect = inner_surface.adjusted(8, 8, -8, -42)
        accent_path = QPainterPath()
        accent_path.addRoundedRect(accent_rect, 8, 8)
        accent_color = QColor("#FFFFFF")
        accent_color.setAlpha(32)
        painter.fillPath(accent_path, accent_color)

        outer_rim_pen = QPen(colors["rim"], 1.2)
        painter.setPen(outer_rim_pen)
        painter.drawRoundedRect(key_rect.adjusted(1, 1, -1, -1), 15, 15)

        inner_rim_pen = QPen(QColor(255, 255, 255, 90), 1.0)
        painter.setPen(inner_rim_pen)
        painter.drawRoundedRect(inner_surface.adjusted(1, 1, -1, -1), 11, 11)

        legend_rect = key_rect.adjusted(12, 8, -12, -18)
        painter.setPen(legend_color)
        title_font = QFont("Segoe UI", 18, QFont.Bold)
        painter.setFont(title_font)
        painter.drawText(legend_rect, Qt.AlignCenter, self._title.split()[-1][-1])
