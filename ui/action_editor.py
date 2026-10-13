import json
from pathlib import Path
from PySide6.QtWidgets import (QDialog, QComboBox, QLineEdit, QPlainTextEdit,
    QSpinBox, QListWidget, QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton,
    QDialogButtonBox, QFileDialog, QLabel, QMessageBox, QFrame, QTabBar)
from PySide6.QtCore import QSize
from input.actions import ACTION_TYPES, MEDIA, AUDIO, INPUT_LABELS, normalize_action


class ActionEditor(QDialog):
    """Edit a snapshot; Cancel never mutates live mappings."""
    def __init__(self, actions, profile_names, parent=None, rotary_only=False):
        super().__init__(parent)
        self.rotary_only = rotary_only
        self.input_labels = INPUT_LABELS[6:] if rotary_only else INPUT_LABELS[:len(actions)]
        self.setWindowTitle("KeyBloom — Rotary Actions" if rotary_only else "KeyBloom — Action Mapping")
        self.resize(980, 720)
        self.setMinimumSize(860, 650)
        self.setObjectName("actionEditor")
        self.setStyleSheet("""
            QDialog#actionEditor { background: #f2effc; }
            QWidget { font-family: 'Segoe UI'; font-size: 13px; color: #2b2545; }
            QFrame#card { background: #ffffff; border: 1px solid #ded7ef; border-radius: 14px; }
            QLabel { background: transparent; border: none; }
            QLabel#heading { font-size: 23px; font-weight: 700; }
            QLabel#sectionTitle { font-size: 18px; font-weight: 600; }
            QLabel#muted { color: #706584; }
            QLineEdit, QPlainTextEdit, QComboBox, QSpinBox {
                background: #faf8ff; border: 1px solid #d8cfe9; border-radius: 7px;
                padding: 8px; selection-background-color: #8e7ab5;
            }
            QLineEdit:focus, QPlainTextEdit:focus, QComboBox:focus, QSpinBox:focus {
                border: 1px solid #8e7ab5;
            }
            QComboBox QAbstractItemView { background: white; color: #2b2545;
                selection-background-color: #e6e1f4; selection-color: #2b2545; }
            QListWidget { background: transparent; border: none; outline: none; }
            QListWidget::item { padding: 10px; margin: 3px 0; border-radius: 8px; }
            QListWidget::item:hover { background: #f2effc; }
            QListWidget::item:selected { background: #e6e1f4; color: #4b3f8f; }
            QTabBar::tab { background: #f2effc; padding: 8px 10px; margin: 2px;
                border-radius: 6px; color: #706584; }
            QTabBar::tab:selected { background: #65518f; color: white; }
            QPushButton { background: #f2effc; border: 1px solid #d8cfe9;
                border-radius: 7px; padding: 8px 12px; font-weight: 600; }
            QPushButton:hover { background: #e6e1f4; border-color: #8e7ab5; }
            QPushButton:pressed { background: #d3caf0; }
            QPushButton:focus { border: 1px solid #65518f; }
            QPushButton:disabled { color: #aaa1b8; background: #f8f6fc; }
            QPushButton#primary { background: #65518f; color: white; border-color: #65518f; }
            QPushButton#primary:hover { background: #7660a3; }
        """)
        self.actions = [normalize_action(a) for a in actions]
        self.current = -1
        self.clipboard = None
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(16)
        heading = QLabel("Rotary Actions" if rotary_only else "Button Actions" if len(actions) == 6 else "Button & Rotary Actions")
        heading.setObjectName("heading")
        layout.addWidget(heading)
        self.profile_caption = QLabel("Customize the controls for your profile")
        self.profile_caption.setObjectName("muted")
        layout.addWidget(self.profile_caption)
        toolbar = QHBoxLayout()
        self.profile_tools = toolbar
        toolbar.addStretch()
        for title, callback in (("Import profile", self.import_profile), ("Export profile", self.export_profile)):
            button = QPushButton(title)
            button.setAutoDefault(False)
            button.clicked.connect(callback)
            toolbar.addWidget(button)
        layout.addLayout(toolbar)
        body = QHBoxLayout()
        body.setSpacing(18)
        layout.addLayout(body, 1)
        navigation = QFrame()
        navigation.setObjectName("card")
        navigation.setFixedWidth(330)
        navigation_layout = QVBoxLayout(navigation)
        navigation_layout.setContentsMargins(12, 16, 12, 12)
        title = QLabel("Controls")
        title.setObjectName("sectionTitle")
        navigation_layout.addWidget(title)
        self.groups = QTabBar()
        group_titles = ("Rotary 1", "Rotary 2") if rotary_only else ("All", "Buttons", "Rotary 1", "Rotary 2")
        for title in group_titles:
            self.groups.addTab(title)
        self.groups.setExpanding(False)
        navigation_layout.addWidget(self.groups)
        self.inputs = QListWidget()
        self.inputs.addItems(self.input_labels)
        self.inputs.setWordWrap(True)
        navigation_layout.addWidget(self.inputs, 1)
        body.addWidget(navigation)
        panel = QFrame()
        panel.setObjectName("card")
        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(22, 20, 22, 20)
        panel_layout.setSpacing(14)
        self.input_title = QLabel()
        self.input_title.setObjectName("sectionTitle")
        panel_layout.addWidget(self.input_title)
        self.input_hint = QLabel()
        self.input_hint.setObjectName("muted")
        self.input_hint.setWordWrap(True)
        panel_layout.addWidget(self.input_hint)
        form = QFormLayout()
        self.form = form
        form.setSpacing(12)
        self.label = QLineEdit()
        self.label.setPlaceholderText("Optional name, e.g. Volume or Next track")
        self.kind = QComboBox()
        for key, title in ACTION_TYPES.items():
            self.kind.addItem(title, key)
        self.choice = QComboBox()
        self.value = QPlainTextEdit()
        self.value.setMinimumHeight(100)
        self.value.setMaximumHeight(150)
        self.value.setPlaceholderText("Shortcut: Ctrl+Shift+S; path, URL, or text")
        self.step = QSpinBox()
        self.step.setRange(1, 100)
        self.step.setSuffix(" %")
        form.addRow("Display name", self.label)
        form.addRow("Action type", self.kind)
        form.addRow("Action", self.choice)
        form.addRow("Value", self.value)
        form.addRow("Spotify volume step", self.step)
        panel_layout.addLayout(form)
        self.action_help = QLabel()
        self.action_help.setObjectName("muted")
        self.action_help.setWordWrap(True)
        panel_layout.addWidget(self.action_help)
        self.profile_names = profile_names
        self.browse_tools = QFrame()
        browse_row = QHBoxLayout(self.browse_tools)
        browse_row.setContentsMargins(0, 0, 0, 0)
        for title, callback in (("Browse file…", self.browse), ("Browse folder…", self.browse_folder)):
            button = QPushButton(title)
            button.setAutoDefault(False)
            button.clicked.connect(callback)
            browse_row.addWidget(button)
        panel_layout.addWidget(self.browse_tools)
        panel_layout.addStretch()
        row = QHBoxLayout()
        for title, callback in (("Copy action", self.copy), ("Paste action", self.paste), ("Clear", self.clear)):
            button = QPushButton(title)
            button.setAutoDefault(False)
            button.clicked.connect(callback)
            row.addWidget(button)
            if callback == self.paste:
                self.paste_button = button
                button.setEnabled(False)
        panel_layout.addLayout(row)
        body.addWidget(panel, 1)
        note = QLabel("Text is typed into the focused application. Media uses the Windows media session.\n"
                      "Held buttons currently repeat; use a brief press for toggle actions.")
        note.setWordWrap(True)
        note.setObjectName("muted")
        layout.addWidget(note)
        buttons = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        buttons.button(QDialogButtonBox.Save).setText("Save Changes")
        buttons.button(QDialogButtonBox.Save).setObjectName("primary")
        buttons.button(QDialogButtonBox.Save).setDefault(True)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.kind.currentIndexChanged.connect(self.configure_kind)
        self.choice.currentIndexChanged.connect(self.configure_step)
        self.inputs.currentRowChanged.connect(self.select)
        self.groups.currentChanged.connect(self.filter_inputs)
        self.inputs.setCurrentRow(0)
        if rotary_only:
            self.filter_inputs(0)
        elif len(actions) == 6:
            self.groups.hide()

    def filter_inputs(self, group):
        ranges = (range(3), range(3, 6)) if self.rotary_only else (range(12), range(6), range(6, 9), range(9, 12))
        visible = ranges[group]
        for index in range(self.inputs.count()):
            self.inputs.item(index).setHidden(index not in visible)
        if self.current not in visible:
            self.inputs.setCurrentRow(visible.start)

    def configure_step(self):
        visible = self.kind.currentData() == "audio" and self.choice.currentData() in ("spotify_up", "spotify_down")
        self.form.setRowVisible(self.step, visible)

    def configure_kind(self):
        mode = self.kind.currentData()
        self.choice.clear()
        choices = MEDIA if mode == "media" else AUDIO if mode == "audio" else {}
        if mode == "profile":
            choices = {"Next profile": "next", **{f"{i}: {name}": str(i)
                       for i, name in enumerate(self.profile_names, 1)}}
        for title, value in choices.items():
            self.choice.addItem(title, value)
        self.form.setRowVisible(self.choice, bool(choices))
        self.form.setRowVisible(self.value, mode in ("shortcut", "application", "url", "text"))
        hints = {
            "none": ("", "This control is disabled. Choose an action type to assign it."),
            "shortcut": ("Ctrl+Shift+S", "Enter a keyboard combination, e.g. Ctrl+C or Ctrl+Shift+S."),
            "application": ("C:\\path\\to\\application.exe", "Choose an application, file, or folder to open."),
            "url": ("https://example.com", "Open a website in your default browser."),
            "text": ("Enter the text to type…", "Text is typed exactly as entered, including spaces and line breaks."),
            "media": ("", "Control playback using the Windows media session."),
            "audio": ("", "Adjust system audio or Spotify volume. Spotify step is applied per turn or press."),
            "profile": ("", "Switch to a specific profile or cycle to the next profile."),
        }
        placeholder, help_text = hints.get(mode, ("", ""))
        self.value.setPlaceholderText(placeholder)
        self.action_help.setText(help_text)
        self.browse_tools.setVisible(mode == "application")
        self.configure_step()

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
            self.inputs.item(index).setText(f"{self.input_labels[index]}\n{summary.splitlines()[0][:42] if summary else 'None'}")
            self.inputs.item(index).setSizeHint(QSize(280, 62))
            self.inputs.item(index).setToolTip(f"{ACTION_TYPES[action['mode']]}: {action['value']}")

    def select(self, index):
        if index < 0:
            return
        self.store()
        self.current = index
        self.load()

    def load(self):
        self.refresh_list()
        action = self.actions[self.current]
        self.input_title.setText(self.input_labels[self.current])
        self.input_hint.setText("Choose what happens when you press this button." if not self.rotary_only and self.current < 6 else
                                "Choose what happens when you turn or press this rotary encoder.")
        self.label.setText(action["label"])
        self.kind.setCurrentIndex(self.kind.findData(action["mode"]))
        self.configure_kind()
        index = self.choice.findData(action["value"])
        if index >= 0:
            self.choice.setCurrentIndex(index)
        self.value.setPlainText(action["value"])
        self.step.setValue(action["step"])
        self.refresh_list()

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
        self.paste_button.setEnabled(True)

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
            Path(path).write_text(json.dumps({"format": "keybloom-rotary-actions-v1" if self.rotary_only else "keybloom-actions-v1", "actions": self.actions},
                                            ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError as error:
            QMessageBox.warning(self, "Export failed", str(error))

    def import_profile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Import action profile", "", "JSON (*.json)")
        if not path:
            return
        try:
            data = json.loads(Path(path).read_text(encoding="utf-8"))
            expected_format = "keybloom-rotary-actions-v1" if self.rotary_only else "keybloom-actions-v1"
            if not isinstance(data, dict) or data.get("format") != expected_format:
                raise ValueError("Not a KeyBloom action profile")
            actions = data.get("actions")
            if not isinstance(actions, list) or len(actions) != len(self.input_labels) or not all(isinstance(a, dict) for a in actions):
                raise ValueError(f"Profile must contain {len(self.input_labels)} actions")
            self.actions = [normalize_action(a) for a in actions]
            self.load()
        except (OSError, ValueError) as error:
            QMessageBox.warning(self, "Import failed", str(error))

    def accept(self):
        self.store()
        super().accept()
