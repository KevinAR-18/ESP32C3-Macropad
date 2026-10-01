from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QDialog, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QVBoxLayout,
)


class ConnectionDialog(QDialog):
    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.setWindowTitle("KeyBloom — Connection")
        self.setMinimumWidth(480)
        layout = QVBoxLayout(self)
        self.status = QLabel("Searching…")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.saved = QLabel()
        layout.addWidget(self.saved)
        self.devices = QComboBox()
        layout.addWidget(self.devices)
        actions = QHBoxLayout()
        for title, callback in (
            ("Scan", lambda: manager.worker.commands.put(("scan", None))),
            ("Connect", self.connect_selected),
            ("Disconnect", lambda: manager.disconnect_device()),
            ("Forget device", lambda: manager.disconnect_device(forget=True)),
        ):
            button = QPushButton(title)
            button.clicked.connect(callback)
            actions.addWidget(button)
        layout.addLayout(actions)
        form = QFormLayout()
        self.auto_sleep = QCheckBox("Enable deep sleep")
        self.auto_sleep.setChecked(manager.settings["auto_sleep"])
        self.idle = QSpinBox()
        self.idle.setRange(10, 3600)
        self.idle.setSuffix(" seconds")
        self.idle.setValue(manager.settings["idle_seconds"])
        self.sleep = QSpinBox()
        self.sleep.setRange(self.idle.value() + 1, 86400)
        self.sleep.setSuffix(" seconds")
        self.sleep.setValue(manager.settings["sleep_seconds"])
        self.idle.valueChanged.connect(lambda value: self.sleep.setMinimum(value + 1))
        form.addRow(self.auto_sleep)
        form.addRow("Connected low-power idle", self.idle)
        form.addRow("Deep sleep after", self.sleep)
        layout.addLayout(form)
        note = QLabel("Deep sleep disconnects BLE. Click encoder 1 to wake.\n"
                      "The wake click does not execute a macro. USB takes priority.")
        note.setWordWrap(True)
        layout.addWidget(note)
        apply = QPushButton("Save power settings")
        apply.clicked.connect(self.save_power)
        layout.addWidget(apply)
        manager.status.connect(self.status.setText)
        manager.devices.connect(self.show_devices)
        manager.changed.connect(self.refresh_saved)
        self.refresh_saved()

    def refresh_saved(self):
        s = self.manager.settings
        self.saved.setText(f"Saved: {s['name']} — {s['address']}" if s["address"] else "No saved BLE device")
        if self.devices.count() == 0 and s["address"]:
            self.devices.addItem(f"{s['name']} ({s['address']})", s["address"])

    def show_devices(self, devices):
        self.devices.clear()
        for address, name in devices:
            self.devices.addItem(f"{name} ({address})", address)
        self.refresh_saved()

    def connect_selected(self):
        self.manager.connect_device(self.devices.currentData() or self.manager.settings["address"])

    def save_power(self):
        self.manager.settings.update(auto_sleep=self.auto_sleep.isChecked(),
                                     idle_seconds=self.idle.value(), sleep_seconds=self.sleep.value())
        self.manager.send_settings()
        self.manager.changed.emit()
