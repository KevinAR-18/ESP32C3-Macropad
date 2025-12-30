import serial
import keyboard
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# ===== SERIAL CONFIG =====
SERIAL_PORT = "COM6"
BAUDRATE = 115200

ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

# ===== GET SPOTIFY AUDIO SESSION =====
def get_spotify_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == "spotify.exe":
            return session._ctl.QueryInterface(ISimpleAudioVolume)
    return None

spotify_volume = get_spotify_volume()

print("Listening from ESP32...")

while True:
    if ser.in_waiting:
        line = ser.readline().decode(errors="ignore").strip()
        print("RX:", line)

        # ===== BUTTONS (TETAP) =====
        if line == "BUTTON 1 PRESSED":
            keyboard.press_and_release("v")

        elif line == "BUTTON 2 PRESSED":
            keyboard.press_and_release("a")

        elif line == "BUTTON 3 PRESSED":
            keyboard.press_and_release("n")

        elif line == "BUTTON 4 PRESSED":
            keyboard.press_and_release("y")

        # ===== ENCODER (SPOTIFY ONLY, NO KEYBOARD) =====
        elif line == "ENCODER RIGHT":
            if spotify_volume:
                vol = spotify_volume.GetMasterVolume()
                spotify_volume.SetMasterVolume(min(vol + 0.03, 1.0), None)

        elif line == "ENCODER LEFT":
            if spotify_volume:
                vol = spotify_volume.GetMasterVolume()
                spotify_volume.SetMasterVolume(max(vol - 0.03, 0.0), None)

        elif line == "ENCODER BUTTON PRESSED":
            keyboard.press_and_release("space")  # play/pause (opsional)
