import re

SHORTCUT_TOKEN_MAP = {
    "win": "windows",
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "pageup": "page up",
    "pagedown": "page down",
    "space": "space",
    "tab": "tab",
    "shift": "shift",
    "ctrl": "ctrl",
    "alt": "alt",
    "enter": "enter",
    "esc": "esc",
    "backspace": "backspace",
    "delete": "delete",
    "insert": "insert",
    "home": "home",
    "end": "end",
    "capslock": "caps lock",
    "numlock": "num lock",
    "scrolllock": "scroll lock",
    "printscreen": "print screen",
    "pause": "pause",
    "menu": "menu",
    "media previous": "previous track",
    "mediaprevious": "previous track",
    "previoustrack": "previous track",
    "previous track": "previous track",
    "media next": "next track",
    "medianext": "next track",
    "nexttrack": "next track",
    "next track": "next track",
    "media play pause": "play/pause media",
    "media-play-pause": "play/pause media",
    "media_play_pause": "play/pause media",
    "playpause": "play/pause media",
    "toggle media play/pause": "play/pause media",
    "play/pause media": "play/pause media",
    "mediaplaypause": "play/pause media",
    "media volume up": "volume up",
    "media volume down": "volume down",
    "media volume mute": "volume mute",
    "volumeup": "volume up",
    "volume up": "volume up",
    "volumedown": "volume down",
    "volume down": "volume down",
    "volumemute": "volume mute",
    "volume mute": "volume mute",
}

GLOBAL_MEDIA_KEY_DISPLAY = {
    "previous track": "Media Previous",
    "next track": "Media Next",
    "play/pause media": "Media Play Pause",
    "volume up": "Volume Up",
    "volume down": "Volume Down",
    "volume mute": "Volume Mute",
}


def _collapse_token(text: str) -> str:
    return re.sub(r"[\s_-]+", "", text.lower())


def normalize_shortcut(shortcut_text: str) -> str:
    text = shortcut_text.strip()
    if not text:
        return ""

    mapped_value = SHORTCUT_TOKEN_MAP.get(text.lower())
    if mapped_value:
        return mapped_value

    mapped_value = SHORTCUT_TOKEN_MAP.get(_collapse_token(text))
    if mapped_value:
        return mapped_value

    normalized_parts = []
    for part in text.split("+"):
        token = part.strip()
        if not token:
            continue

        mapped_token = SHORTCUT_TOKEN_MAP.get(token.lower())
        if mapped_token:
            normalized_parts.append(mapped_token)
            continue

        mapped_token = SHORTCUT_TOKEN_MAP.get(_collapse_token(token))
        if mapped_token:
            normalized_parts.append(mapped_token)
            continue

        if re.fullmatch(r"F\d{1,2}", token, re.IGNORECASE):
            normalized_parts.append(token.lower())
            continue

        if len(token) == 1:
            normalized_parts.append(token.lower())
            continue

        normalized_parts.append(token.lower())

    return "+".join(normalized_parts)


def global_event_to_shortcut_text(event_name: str | None) -> str:
    if not event_name:
        return ""
    normalized_name = normalize_shortcut(event_name)
    return GLOBAL_MEDIA_KEY_DISPLAY.get(normalized_name, "")
