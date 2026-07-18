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
APP_NAME = "KeyBloom"


def legacy_app_config_path(filename: str) -> str:
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(base_dir, filename)


def app_config_dir() -> str:
    # Roaming AppData is safer for packaged Windows apps because Program Files
    # or other install folders may not be writable.
    roaming_appdata = os.getenv("APPDATA")
    if roaming_appdata:
        return os.path.join(roaming_appdata, APP_NAME)

    local_appdata = os.getenv("LOCALAPPDATA")
    if local_appdata:
        return os.path.join(local_appdata, APP_NAME)

    return os.path.join(os.path.expanduser("~"), f".{APP_NAME.lower()}")


def app_config_path(filename: str) -> str:
    return os.path.join(app_config_dir(), filename)


def settings_path() -> str:
    return app_config_path("settings.json")


def legacy_settings_path() -> str:
    return legacy_app_config_path("settings.json")


def load_settings(path: str):
    # Prefer the AppData file, but still accept a legacy settings file placed
    # next to the script or executable.
    candidate_paths = [path]
    legacy_path = legacy_settings_path()
    if legacy_path not in candidate_paths:
        candidate_paths.append(legacy_path)

    existing_path = next((candidate for candidate in candidate_paths if os.path.exists(candidate)), None)
    if not existing_path:
        return None
    try:
        with open(existing_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return None


def save_settings(path: str, data: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
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
        if mode == SHORTCUT_MODE:
            value = _normalize_loaded_shortcut(value)
        return {"mode": mode, "value": value}

    return {"mode": SHORTCUT_MODE, "value": _normalize_loaded_shortcut(str(entry or ""))}


def _normalize_loaded_shortcut(value: str) -> str:
    # Keep application targets and empty values untouched; only normalize
    # shortcut text so legacy/raw values stored in settings become valid
    # tokens understood by the keyboard module.
    if not value:
        return value
    try:
        from input.shortcut_utils import normalize_shortcut
    except ImportError:
        return value
    normalized = normalize_shortcut(value)
    return normalized or value


def _format_loaded_display(value: str) -> str:
    if not value:
        return value
    try:
        from input.shortcut_utils import format_shortcut_display
    except ImportError:
        return value
    return format_shortcut_display(value)


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
                display_value = entry["value"]
                if entry["mode"] == SHORTCUT_MODE:
                    display_value = _format_loaded_display(entry["value"])
                slot["line_edit"].setText(display_value)


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
