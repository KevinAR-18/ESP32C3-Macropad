"""Standalone popup checks without serial or hardware dependencies."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import unittest
from PySide6.QtWidgets import QApplication
from input.actions import default_rotary
from ui.action_editor import ActionEditor


class ActionEditorUITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.original = [{"mode": "none", "value": ""} for _ in range(6)] + default_rotary()
        self.editor = ActionEditor(self.original, ["One", "Two", "Three", "Four", "Five"])

    def tearDown(self):
        self.editor.close()

    def test_navigation_stores_edits_and_filters_controls(self):
        self.editor.kind.setCurrentIndex(self.editor.kind.findData("text"))
        self.editor.value.setPlainText("  Hello\nworld  ")
        self.editor.groups.setCurrentIndex(2)
        self.assertEqual(self.editor.current, 6)
        self.assertEqual(self.editor.actions[0]["value"], "  Hello\nworld  ")
        self.assertTrue(self.editor.inputs.item(0).isHidden())
        self.assertFalse(self.editor.inputs.item(6).isHidden())
        self.assertEqual(self.editor.input_title.text(), "Rotary 1 — Left")
        self.editor.groups.setCurrentIndex(3)
        self.assertEqual(self.editor.current, 9)
        self.editor.groups.setCurrentIndex(0)
        self.assertTrue(all(not self.editor.inputs.item(i).isHidden() for i in range(12)))

    def test_fields_follow_action_and_spotify_selection(self):
        self.editor.kind.setCurrentIndex(self.editor.kind.findData("application"))
        self.assertFalse(self.editor.browse_tools.isHidden())
        self.assertTrue(self.editor.form.isRowVisible(self.editor.value))
        self.assertFalse(self.editor.form.isRowVisible(self.editor.choice))
        self.editor.inputs.setCurrentRow(6)
        self.assertFalse(self.editor.form.isRowVisible(self.editor.step))
        self.editor.choice.setCurrentIndex(self.editor.choice.findData("spotify_up"))
        self.assertTrue(self.editor.form.isRowVisible(self.editor.step))
        self.editor.choice.setCurrentIndex(self.editor.choice.findData("volume mute"))
        self.assertFalse(self.editor.form.isRowVisible(self.editor.step))

    def test_copy_paste_and_cancel_leave_original_unchanged(self):
        self.assertFalse(self.editor.paste_button.isEnabled())
        self.editor.kind.setCurrentIndex(self.editor.kind.findData("media"))
        self.editor.choice.setCurrentIndex(self.editor.choice.findData("next track"))
        self.editor.copy()
        self.assertTrue(self.editor.paste_button.isEnabled())
        self.editor.inputs.setCurrentRow(1)
        self.editor.paste()
        self.assertEqual(self.editor.actions[1]["value"], "next track")
        self.editor.reject()
        self.assertEqual(self.original[0]["mode"], "none")
        self.assertEqual(self.original[1]["mode"], "none")

    def test_rotary_only_navigation_and_snapshot(self):
        editor = ActionEditor(default_rotary(), ["One", "Two"], rotary_only=True)
        try:
            self.assertEqual(editor.inputs.count(), 6)
            self.assertEqual(editor.groups.count(), 2)
            self.assertEqual(editor.input_title.text(), "Rotary 1 — Left")
            self.assertTrue(editor.inputs.item(3).isHidden())
            editor.groups.setCurrentIndex(1)
            self.assertEqual(editor.current, 3)
            self.assertEqual(editor.input_title.text(), "Rotary 2 — Left")
            self.assertTrue(editor.inputs.item(0).isHidden())
            self.assertFalse(editor.inputs.item(3).isHidden())
            editor.accept()
            self.assertEqual(len(editor.actions), 6)
        finally:
            editor.close()


if __name__ == "__main__":
    unittest.main()
