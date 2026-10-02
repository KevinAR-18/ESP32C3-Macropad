import json
from pathlib import Path
from PySide6.QtWidgets import (QDialog, QComboBox, QLineEdit, QPlainTextEdit,
    QSpinBox, QListWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton,
    QDialogButtonBox, QFileDialog, QLabel, QMessageBox)
from input.actions import ACTION_TYPES, MEDIA, AUDIO, INPUT_LABELS, normalize_action


class ActionEditor(QDialog):
    """Edit a snapshot; Cancel never mutates live mappings."""
    def __init__(self, actions, profile_names, parent=None):
        super().__init__(parent)
        self.setWindowTitle("KeyBloom — Action Mapping")
        self.resize(650, 640)
        self.actions = [normalize_action(a) for a in actions]
        self.current = -1
        self.clipboard = None
        layout = QVBoxLayout(self)
        self.inputs = QListWidget()
        self.inputs.addItems(INPUT_LABELS)
        layout.addWidget(self.inputs)
        form = QFormLayout()
        self.label = QLineEdit()
        self.kind = QComboBox()
        for key, title in ACTION_TYPES.items():
            self.kind.addItem(title, key)
        self.choice = QComboBox()
        self.value = QPlainTextEdit()
        self.value.setMaximumHeight(85)
        self.value.setPlaceholderText("Shortcut: Ctrl+Shift+S; path, URL, or text")
        self.step = QSpinBox()
        self.step.setRange(1, 100)
        self.step.setSuffix(" %")
        form.addRow("Display name", self.label)
        form.addRow("Action type", self.kind)
        form.addRow("Action", self.choice)
        form.addRow("Value", self.value)
        form.addRow("Spotify volume step", self.step)
        layout.addLayout(form)
        self.profile_names = profile_names
        row = QHBoxLayout()
        for title, callback in (("Browse file", self.browse), ("Browse folder", self.browse_folder),
                                ("Copy", self.copy), ("Paste", self.paste), ("Clear", self.clear)):
            button = QPushButton(title)
            button.clicked.connect(callback)
            row.addWidget(button)
        layout.addLayout(row)
        row = QHBoxLayout()
        for title, callback in (("Export profile", self.export_profile), ("Import profile", self.import_profile)):
            button = QPushButton(title)
            button.clicked.connect(callback)
            row.addWidget(button)
        layout.addLayout(row)
        note = QLabel("Text is typed into the focused application. Media uses the Windows media session.\n"
                      "Held buttons currently repeat; use a brief press for toggle actions.")
        note.setWordWrap(True)
        layout.addWidget(note)
        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.kind.currentIndexChanged.connect(self.configure_kind)
        self.inputs.currentRowChanged.connect(self.select)
        self.inputs.setCurrentRow(0)

    def configure_kind(self):
        mode = self.kind.currentData()
        self.choice.clear()
        choices = MEDIA if mode == "media" else AUDIO if mode == "audio" else {}
        if mode == "profile":
            choices = {"Next profile": "next", **{f"{i}: {name}": str(i)
                       for i, name in enumerate(self.profile_names, 1)}}
        for title, value in choices.items():
            self.choice.addItem(title, value)
        self.choice.setVisible(bool(choices))
        self.value.setVisible(mode in ("shortcut", "application", "url", "text"))
        self.step.setVisible(mode == "audio")

    def store(self):
        if self.current < 0:
            return
        mode = self.kind.currentData()
        value = self.choice.currentData() if mode in ("media", "audio", "profile") else self.value.toPlainText()
        self.actions[self.current] = normalize_action({"mode": mode, "value": value or "",
            "label": self.label.text(), "step": self.step.value()})
        self.refresh_list()

    def refresh_list(self):
        for index, action in enumerate(self.actions):
            summary = action["label"] or action["value"] or ACTION_TYPES[action["mode"]]
            self.inputs.item(index).setText(f"{INPUT_LABELS[index]}  ·  {summary.splitlines()[0] if summary else 'None'}")
            self.inputs.item(index).setToolTip(f"{ACTION_TYPES[action['mode']]}: {action['value']}")

    def select(self, index):
        self.store()
        self.current = index
        self.load()

    def load(self):
        self.refresh_list()
        action = self.actions[self.current]
        self.label.setText(action["label"])
        self.kind.setCurrentIndex(self.kind.findData(action["mode"]))
        self.configure_kind()
        index = self.choice.findData(action["value"])
        if index >= 0:
            self.choice.setCurrentIndex(index)
        self.value.setPlainText(action["value"])
        self.step.setValue(action["step"])

    def browse(self):
        path, _ = QFileDialog.getOpenFileName(self, "Choose application or file")
        if path:
            self.kind.setCurrentIndex(self.kind.findData("application"))
            self.value.setPlainText(path)

    def browse_folder(self):
        path = QFileDialog.getExistingDirectory(self, "Choose folder")
        if path:
            self.kind.setCurrentIndex(self.kind.findData("application"))
            self.value.setPlainText(path)

    def copy(self):
        self.store()
        self.clipboard = dict(self.actions[self.current])

    def paste(self):
        if self.clipboard:
            self.actions[self.current] = dict(self.clipboard)
            self.load()

    def clear(self):
        self.actions[self.current] = normalize_action({"mode": "none"})
        self.load()

    def export_profile(self):
        self.store()
        path, _ = QFileDialog.getSaveFileName(self, "Export action profile", "keybloom-profile.json", "JSON (*.json)")
        if not path:
            return
        try:
            Path(path).write_text(json.dumps({"format": "keybloom-actions-v1", "actions": self.actions},
                                            ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError as error:
            QMessageBox.warning(self, "Export failed", str(error))

    def import_profile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import action profile", "", "JSON (*.json)")
        if not path:
            return
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("format") != "keybloom-actions-v1":
                raise ValueError("Not a KeyBloom action profile")
            actions = data.get("actions")
            if not isinstance(actions, list) or len(actions) != 12 or not all(isinstance(a, dict) for a in actions):
                raise ValueError("Profile must contain 12 actions")
            self.actions = [normalize_action(a) for a in actions]
            self.load()
        except (OSError, ValueError) as error:
            QMessageBox.warning(self, "Import failed", str(error))

    def accept(self):
        self.store()
        super().accept()
