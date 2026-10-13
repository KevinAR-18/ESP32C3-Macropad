from PySide6.QtWidgets import (
    QCheckBox, QComboBox, QDialog, QFormLayout, QHBoxLayout, QLabel,
    QPushButton, QSpinBox, QVBoxLayout, QFrame,
)


class ConnectionDialog(QDialog):
    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.setWindowTitle("KeyBloom — Connection")
        self.setMinimumWidth(560)
        self.resize(620, 680)
        self.setObjectName("connectionDialog")
        self.setStyleSheet("""
            QDialog#connectionDialog { background: #f2effc; }
            QWidget { font-family: 'Segoe UI'; font-size: 13px; color: #2b2545; }
            QFrame#card { background: white; border: 1px solid #ded7ef; border-radius: 14px; }
            QLabel { background: transparent; border: none; }
            QLabel#heading { font-size: 23px; font-weight: 700; }
            QLabel#sectionTitle { font-size: 17px; font-weight: 600; }
            QLabel#muted { color: #706584; }
            QLabel#status { background: #e6e1f4; color: #4b3f8f; padding: 12px;
                border: 1px solid #d8cfe9; border-radius: 8px; font-weight: 600; }
            QComboBox, QSpinBox { background: #faf8ff; border: 1px solid #d8cfe9;
                border-radius: 7px; padding: 8px; selection-background-color: #8e7ab5; }
            QComboBox:focus, QSpinBox:focus { border-color: #65518f; }
            QComboBox QAbstractItemView { background: white; color: #2b2545;
                selection-background-color: #e6e1f4; selection-color: #2b2545; }
            QCheckBox { background: transparent; spacing: 8px; }
            QCheckBox::indicator { width: 17px; height: 17px; border-radius: 4px;
                border: 1px solid #b9a9d4; background: #faf8ff; }
            QCheckBox::indicator:checked { background: #65518f; border-color: #65518f; }
            QPushButton { background: #f2effc; border: 1px solid #d8cfe9;
                border-radius: 7px; padding: 9px 14px; font-weight: 600; }
            QPushButton:hover { background: #e6e1f4; border-color: #8e7ab5; }
            QPushButton:pressed { background: #d3caf0; }
            QPushButton:focus { border-color: #65518f; }
            QPushButton:disabled { color: #aaa1b8; background: #f8f6fc; }
            QPushButton#primary { background: #65518f; color: white; border-color: #65518f; }
            QPushButton#primary:hover { background: #7660a3; }
            QPushButton#danger { color: #a14e65; background: #fff7fa; border-color: #ead0d9; }
            QPushButton#danger:hover { background: #f8e6ed; }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 22, 24, 20)
        layout.setSpacing(16)
        heading = QLabel("Bluetooth Connection")
        heading.setObjectName("heading")
        layout.addWidget(heading)
        subtitle = QLabel("Connect your KeyBloom wirelessly and manage power settings.")
        subtitle.setObjectName("muted")
        subtitle.setWordWrap(True)
        layout.addWidget(subtitle)
        self.status = QLabel("Searching…")
        self.status.setObjectName("status")
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        device_card = QFrame()
        device_card.setObjectName("card")
        device_layout = QVBoxLayout(device_card)
        device_layout.setContentsMargins(20, 18, 20, 18)
        device_layout.setSpacing(12)
        device_title = QLabel("Device")
        device_title.setObjectName("sectionTitle")
        device_layout.addWidget(device_title)
        self.saved = QLabel()
        self.saved.setObjectName("muted")
        self.saved.setWordWrap(True)
        device_layout.addWidget(self.saved)
        device_layout.addWidget(QLabel("Available Bluetooth devices"))
        self.devices = QComboBox()
        self.devices.setPlaceholderText("Scan to find your KeyBloom…")
        device_layout.addWidget(self.devices)
        actions = QHBoxLayout()
        for title, callback in (
            ("Scan devices", lambda: manager.worker.commands.put(("scan", None))),
            ("Connect", self.connect_selected),
        ):
            button = QPushButton(title)
            button.setAutoDefault(False)
            if title == "Connect":
                button.setObjectName("primary")
                self.connect_button = button
            button.clicked.connect(callback)
            actions.addWidget(button)
        device_layout.addLayout(actions)
        secondary = QHBoxLayout()
        secondary.addStretch()
        for title, callback in (
            ("Disconnect", lambda: manager.disconnect_device()),
            ("Forget device", lambda: manager.disconnect_device(forget=True)),
        ):
            button = QPushButton(title)
            button.setAutoDefault(False)
            if title == "Forget device":
                button.setObjectName("danger")
            button.clicked.connect(callback)
            secondary.addWidget(button)
        device_layout.addLayout(secondary)
        layout.addWidget(device_card)
        power_card = QFrame()
        power_card.setObjectName("card")
        power_layout = QVBoxLayout(power_card)
        power_layout.setContentsMargins(20, 18, 20, 18)
        power_layout.setSpacing(12)
        power_title = QLabel("Power Settings")
        power_title.setObjectName("sectionTitle")
        power_layout.addWidget(power_title)
        form = QFormLayout()
        form.setSpacing(12)
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
        self.sleep.setEnabled(self.auto_sleep.isChecked())
        self.auto_sleep.toggled.connect(self.sleep.setEnabled)
        self.idle.valueChanged.connect(lambda value: self.sleep.setMinimum(value + 1))
        form.addRow(self.auto_sleep)
        form.addRow("Connected low-power idle", self.idle)
        form.addRow("Deep sleep after", self.sleep)
        power_layout.addLayout(form)
        note = QLabel("Deep sleep disconnects BLE. Click encoder 1 to wake.\n"
                      "The wake click does not execute a macro. USB takes priority.")
        note.setWordWrap(True)
        note.setObjectName("muted")
        power_layout.addWidget(note)
        apply = QPushButton("Save power settings")
        apply.setObjectName("primary")
        apply.setAutoDefault(False)
        apply.clicked.connect(self.save_power)
        power_layout.addWidget(apply)
        layout.addWidget(power_card)
        footer = QHBoxLayout()
        footer.addStretch()
        close = QPushButton("Close")
        close.setAutoDefault(False)
        close.clicked.connect(self.reject)
        footer.addWidget(close)
        layout.addLayout(footer)
        self.devices.currentIndexChanged.connect(self.update_connect_button)
        manager.status.connect(self.status.setText)
        manager.devices.connect(self.show_devices)
        manager.changed.connect(self.refresh_saved)
        self.refresh_saved()

    def refresh_saved(self):
        s = self.manager.settings
        self.saved.setText(f"Saved: {s['name']} — {s['address']}" if s["address"] else "No saved BLE device")
        if self.devices.count() == 0 and s["address"]:
            self.devices.addItem(f"{s['name']} ({s['address']})", s["address"])
            self.devices.setCurrentIndex(0)
        self.update_connect_button()

    def update_connect_button(self):
        self.connect_button.setEnabled(bool(self.devices.currentData() or self.manager.settings["address"]))

    def show_devices(self, devices):
        self.devices.clear()
        for address, name in devices:
            self.devices.addItem(f"{name} ({address})", address)
        if self.devices.count():
            saved_index = self.devices.findData(self.manager.settings["address"])
            self.devices.setCurrentIndex(saved_index if saved_index >= 0 else 0)
        self.refresh_saved()

    def connect_selected(self):
        self.manager.connect_device(self.devices.currentData() or self.manager.settings["address"])

    def save_power(self):
        self.manager.settings.update(auto_sleep=self.auto_sleep.isChecked(),
                                     idle_seconds=self.idle.value(), sleep_seconds=self.sleep.value())
        self.manager.send_settings()
        self.manager.changed.emit()
