import serial
import keyboard
import json
import os
import time
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# ================= SERIAL =================
SERIAL_PORT = "COM6"
BAUDRATE = 115200
ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

# ================= PATH =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEYMAP_PATH = os.path.join(BASE_DIR, "keymap.json")

# ================= LOAD KEYMAP =================
button_map = {}
keymap_mtime = 0

def load_keymap():
    global button_map, keymap_mtime
    try:
        mtime = os.path.getmtime(KEYMAP_PATH)
        if mtime != keymap_mtime:
            with open(KEYMAP_PATH, "r") as f:
                button_map = json.load(f)
            keymap_mtime = mtime
            print("[KEYMAP] Reloaded")
    except Exception as e:
        print("[KEYMAP] Error:", e)

# ================= SPOTIFY =================
def get_spotify_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == "spotify.exe":
            return session._ctl.QueryInterface(ISimpleAudioVolume)
    return None

spotify_volume = get_spotify_volume()

print("Listening from ESP32...")
load_keymap()

# ================= MAIN LOOP =================
while True:
    load_keymap()  # HOT RELOAD CHECK

    if not ser.in_waiting:
        time.sleep(0.01)
        continue

    line = ser.readline().decode(errors="ignore").strip()
    print("RX:", line)

    # ---------- BUTTONS (JSON) ----------
    if line in button_map:
        keyboard.press_and_release(button_map[line])
        continue

    # ---------- ENCODER 1 : SPOTIFY ----------
    if line == "ENC1 RIGHT" and spotify_volume:
        vol = spotify_volume.GetMasterVolume()
        spotify_volume.SetMasterVolume(min(vol + 0.01, 1.0), None)

    elif line == "ENC1 LEFT" and spotify_volume:
        vol = spotify_volume.GetMasterVolume()
        spotify_volume.SetMasterVolume(max(vol - 0.01, 0.0), None)

    elif line == "ENC1 BUTTON PRESSED":
        keyboard.send("play/pause media")

    # ---------- ENCODER 2 : WINDOWS ----------
    elif line == "ENC2 RIGHT":
        keyboard.send("volume up")

    elif line == "ENC2 LEFT":
        keyboard.send("volume down")

    elif line == "ENC2 BUTTON PRESSED":
        keyboard.send("volume mute")
