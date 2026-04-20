import json
import os
import sys

DEFAULT_PROFILE_TITLES = [
    "Custom Title #1",
    "Custom Title #2",
    "Custom Title #3",
    "Custom Title #4",
    "Custom Title #5",
]
SHORTCUT_MODE = "shortcut"
APPLICATION_MODE = "application"


def app_config_path(filename: str) -> str:
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(base_dir, filename)


def settings_path() -> str:
    return app_config_path("settings.json")


def load_settings(path: str):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None


def save_settings(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def collect_profile_names(profile_inputs, defaults=DEFAULT_PROFILE_TITLES):
    names = []
    for idx, line_edit in enumerate(profile_inputs):
        text = line_edit.text().strip()
        names.append(text if text else defaults[idx])
    return names


def apply_profile_titles(title_labels, names):
    for idx, label in enumerate(title_labels):
        label.setText(names[idx])


def normalize_profile_entry(entry):
    if isinstance(entry, dict):
        mode = entry.get("mode", SHORTCUT_MODE)
        value = str(entry.get("value", ""))
        if mode not in {SHORTCUT_MODE, APPLICATION_MODE}:
            mode = SHORTCUT_MODE
        return {"mode": mode, "value": value}

    return {"mode": SHORTCUT_MODE, "value": str(entry or "")}


def collect_profile_mappings(profile_slots):
    mappings = {}
    for profile, slots in profile_slots.items():
        mappings[profile] = [
            {
                "mode": slot.get("mode", SHORTCUT_MODE),
                "value": (
                    slot.get("stored_value", "").strip()
                    if slot.get("mode") == APPLICATION_MODE
                    else slot["line_edit"].text().strip()
                ),
            }
            for slot in slots
        ]
    return mappings


def apply_profile_mappings(profile_slots, mappings):
    for profile, slots in profile_slots.items():
        values = mappings.get(profile, [])
        for idx, slot in enumerate(slots):
            if idx < len(values):
                entry = normalize_profile_entry(values[idx])
                slot["mode"] = entry["mode"]
                slot["stored_value"] = entry["value"]
                slot["line_edit"].setText(entry["value"])


def set_autostart(enabled: bool, app_name: str, app_path: str):
    try:
        import winreg
    except ImportError:
        return

    run_key = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, run_key, 0, winreg.KEY_SET_VALUE) as key:
            if enabled:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
            else:
                try:
                    winreg.DeleteValue(key, app_name)
                except FileNotFoundError:
                    pass
    except OSError:
        pass
