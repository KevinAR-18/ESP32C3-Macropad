"""Offline action/editor integration checks; never type into real applications."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from unittest.mock import patch, Mock
from PySide6.QtWidgets import QApplication, QLineEdit
APP = QApplication.instance() or QApplication([])
from input.actions import default_rotary, ROTARY_EVENTS
from config.settings_manager import apply_profile_mappings, collect_profile_mappings
from ui.action_editor import ActionEditor
import main


class ActionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_round_trip_preserves_text_and_legacy_shortcuts(self):
        slots = {"1": [{"line_edit": QLineEdit()} for _ in range(3)]}
        entries = ["Ctrl+C", {"mode": "text", "value": "  Hello\n世界  ", "label": "Greeting"},
                   {"mode": "audio", "value": "spotify_up", "step": 7}]
        apply_profile_mappings(slots, {"1": entries})
        saved = collect_profile_mappings(slots)["1"]
        self.assertEqual(saved[0]["mode"], "shortcut")
        self.assertEqual(saved[1]["value"], entries[1]["value"])
        self.assertEqual(saved[1]["label"], "Greeting")
        self.assertEqual(saved[2]["step"], 7)

    def test_editor_switch_copy_paste_and_cancel_isolation(self):
        original = [{"mode": "none", "value": ""} for _ in range(6)] + default_rotary()
        editor = ActionEditor(original, ["One", "Two", "Three", "Four", "Five"])
        editor.kind.setCurrentIndex(editor.kind.findData("media"))
        editor.choice.setCurrentIndex(editor.choice.findData("next track"))
        editor.label.setText("Next")
        editor.copy()
        editor.inputs.setCurrentRow(7)
        editor.paste()
        editor.accept()
        self.assertEqual(editor.actions[0]["value"], "next track")
        self.assertEqual(editor.actions[7]["label"], "Next")
        self.assertEqual(original[0]["mode"], "none")

    def test_dispatch_save_load_and_old_rotary_defaults(self):
        with patch("main.load_settings", return_value={}), patch("main.save_settings") as save, \
             patch("connection.manager.list_ports.comports", return_value=[]):
            window = main.MainWindow()
            try:
                window._send_media_key = Mock()
                window._adjust_spotify_volume = Mock()
                for event in ROTARY_EVENTS:
                    window._handle_device_event(event)
                self.assertEqual(window._send_media_key.call_count, 4)
                window._adjust_spotify_volume.assert_any_call(-0.03)
                window._adjust_spotify_volume.assert_any_call(0.03)
                keyboard = Mock()
                window._keyboard = keyboard
                window._execute_action({"mode": "text", "value": "  a\nb  "})
                keyboard.write.assert_called_once_with("  a\nb  ")
                window._execute_action({"mode": "profile", "value": "2"})
                self.assertEqual(window._current_profile_id, "2")
                window._rotary_mappings["2"][0] = {"mode": "media", "value": "previous track"}
                window._handle_device_event("ENC1 LEFT")
                window._send_media_key.assert_called_with("previous track")
                apply_profile_mappings(window._profile_slots, {"2": [{"mode": "text", "value": " text "}]})
                window._refresh_slot_modes()
                window._save_settings()
                data = save.call_args.args[1]
                self.assertEqual(data["profiles"]["2"][0]["value"], " text ")
                with patch("main.load_settings", return_value=data):
                    window._load_settings()
                self.assertEqual(window._rotary_mappings["2"][0]["value"], "previous track")
                self.assertEqual(window._current_profile_id, "1")
            finally:
                window._stop_connections()
                window.tray.hide()
                window.close()


if __name__ == "__main__":
    unittest.main()
