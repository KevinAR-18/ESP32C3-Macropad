from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtWidgets import QLineEdit


class KeyCaptureFilter(QObject):
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