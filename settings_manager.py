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


def settings_path() -> str:
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(base_dir, "settings.json")


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


def collect_profile_mappings(profile_lines):
    mappings = {}
    for profile, lines in profile_lines.items():
        mappings[profile] = [line.text().strip() for line in lines]
    return mappings


def apply_profile_mappings(profile_lines, mappings):
    for profile, lines in profile_lines.items():
        values = mappings.get(profile, [])
        for idx, line in enumerate(lines):
            if idx < len(values):
                line.setText(values[idx])


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