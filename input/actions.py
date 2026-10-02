"""Action definitions shared by the editor and desktop event dispatcher."""
ACTION_TYPES = {
    "none": "None", "shortcut": "Keyboard Shortcut",
    "media": "Media", "audio": "Audio", "application": "Open App / File / Folder",
    "url": "Open URL", "text": "Text", "profile": "Switch Profile",
}
MEDIA = {"Play / Pause": "play/pause media", "Next Track": "next track",
         "Previous Track": "previous track", "Stop": "stop media"}
AUDIO = {"Volume Up": "volume up", "Volume Down": "volume down",
         "Mute": "volume mute", "Spotify Volume Up": "spotify_up",
         "Spotify Volume Down": "spotify_down"}
ROTARY_EVENTS = ("ENC1 LEFT", "ENC1 RIGHT", "ENC1 BUTTON PRESSED",
                 "ENC2 LEFT", "ENC2 RIGHT", "ENC2 BUTTON PRESSED")
INPUT_LABELS = tuple(f"Button {i}" for i in range(1, 7)) + (
    "Rotary 1 — Left", "Rotary 1 — Right", "Rotary 1 — Click",
    "Rotary 2 — Left", "Rotary 2 — Right", "Rotary 2 — Click")


def default_rotary():
    return [{"mode": mode, "value": value, "label": "", "step": 3} for mode, value in (
        ("audio", "volume down"), ("audio", "volume up"), ("audio", "volume mute"),
        ("audio", "spotify_down"), ("audio", "spotify_up"), ("media", "play/pause media"))]


def normalize_action(entry):
    entry = entry if isinstance(entry, dict) else {"value": str(entry or "")}
    mode = entry.get("mode", "shortcut")
    if mode not in ACTION_TYPES:
        mode = "shortcut"
    try:
        step = max(1, min(100, int(entry.get("step", 3))))
    except (ValueError, TypeError):
        step = 3
    return {"mode": mode, "value": str(entry.get("value", "")),
            "label": str(entry.get("label", "")), "step": step}
