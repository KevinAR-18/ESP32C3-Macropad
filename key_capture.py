from PySide6.QtCore import QEvent, QObject, Qt
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QLineEdit


class KeyCaptureFilter(QObject):
    MODIFIER_KEYS = {
        Qt.Key_Control: "Ctrl",
        Qt.Key_Shift: "Shift",
        Qt.Key_Alt: "Alt",
        Qt.Key_Meta: "Win",
    }

    SPECIAL_KEY_NAMES = {
        Qt.Key_Escape: "Esc",
        Qt.Key_Return: "Enter",
        Qt.Key_Enter: "Enter",
        Qt.Key_Space: "Space",
        Qt.Key_Tab: "Tab",
        Qt.Key_Backtab: "Shift+Tab",
        Qt.Key_Backspace: "Backspace",
        Qt.Key_Delete: "Delete",
        Qt.Key_Insert: "Insert",
        Qt.Key_Home: "Home",
        Qt.Key_End: "End",
        Qt.Key_PageUp: "PageUp",
        Qt.Key_PageDown: "PageDown",
        Qt.Key_Left: "Left",
        Qt.Key_Right: "Right",
        Qt.Key_Up: "Up",
        Qt.Key_Down: "Down",
        Qt.Key_CapsLock: "CapsLock",
        Qt.Key_NumLock: "NumLock",
        Qt.Key_ScrollLock: "ScrollLock",
        Qt.Key_Print: "PrintScreen",
        Qt.Key_Pause: "Pause",
        Qt.Key_Menu: "Menu",
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.active_keys = []

    def reset(self):
        self.active_keys.clear()

    def eventFilter(self, obj, event):
        if not isinstance(obj, QLineEdit):
            return super().eventFilter(obj, event)
        if not obj.property("capture_shortcut"):
            return super().eventFilter(obj, event)

        if event.type() == QEvent.ShortcutOverride:
            # Blok shortcut level window/aplikasi seperti Alt+F4 saat field
            # sedang dipakai untuk merekam kombinasi tombol.
            event.accept()
            return True

        if event.type() == QEvent.KeyPress:
            key = event.key()

            if key in (Qt.Key_Backspace, Qt.Key_Delete):
                obj.clear()
                self.active_keys.clear()
                return True

            if key in self.MODIFIER_KEYS:
                self._add_key(key)
                self._update_text(obj, event.modifiers())
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

        modifier_pairs = (
            (Qt.ControlModifier, Qt.Key_Control),
            (Qt.ShiftModifier, Qt.Key_Shift),
            (Qt.AltModifier, Qt.Key_Alt),
            (Qt.MetaModifier, Qt.Key_Meta),
        )
        for modifier_flag, key in modifier_pairs:
            if (modifiers & modifier_flag) or (key in self.active_keys):
                keys.append(self.MODIFIER_KEYS[key])

        for key in self.active_keys:
            if key in self.MODIFIER_KEYS:
                continue
            key_name = self._key_name(key)
            keys.append(key_name)

        if keys:
            obj.setText("+".join(keys))

    def _key_name(self, key):
        if key in self.SPECIAL_KEY_NAMES:
            return self.SPECIAL_KEY_NAMES[key]

        if Qt.Key_F1 <= key <= Qt.Key_F35:
            return f"F{key - Qt.Key_F1 + 1}"

        text = QKeySequence(key).toString(QKeySequence.PortableText)
        if text:
            return text.replace("+", "")

        key_name = Qt.Key(key).name.replace("Key_", "")
        return key_name or str(key)
