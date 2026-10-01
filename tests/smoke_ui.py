"""Offscreen startup/shutdown smoke check, without touching user settings/hardware."""
import os
os.environ["QT_QPA_PLATFORM"] = "offscreen"

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from unittest.mock import patch
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
import main

app = QApplication([])
with patch("main.load_settings", return_value={}), patch("main.save_settings") as save, \
     patch("connection.manager.list_ports.comports", return_value=[]):
    window = main.MainWindow()
    window.connection_dialog.show()
    QTimer.singleShot(250, app.quit)
    app.exec()
    assert not window.connections.worker.isRunning()
    assert save.called
    assert "connection" in save.call_args.args[1]
print("UI startup, connection dialog, settings save, and worker shutdown passed")
