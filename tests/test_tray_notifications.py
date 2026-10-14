"""Tray checks without displaying notifications or connecting to hardware."""
import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from PySide6.QtWidgets import QSystemTrayIcon
from main import APP_VERSION, MainWindow


class TrayNotificationTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual(APP_VERSION, "1.2.0")

    def test_connection_messages(self):
        window = SimpleNamespace(tray=Mock())
        cases = [
            ("USB", "COM3", "auto", "Connected", "Automatically connected via USB to COM3."),
            ("BLE", "KeyBloom-C3", "reconnect", "Reconnected", "Successfully reconnected via Bluetooth to KeyBloom-C3."),
            ("BLE", "KeyBloom-C3", "manual", "Connected", "Successfully connected via Bluetooth to KeyBloom-C3."),
        ]
        for transport, device, kind, title, message in cases:
            with self.subTest(kind=kind):
                MainWindow._show_connection_notification(window, transport, device, kind)
                window.tray.showMessage.assert_called_with(
                    f"KeyBloom — {title}", message, QSystemTrayIcon.Information, 3000
                )
