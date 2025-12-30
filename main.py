import serial
import keyboard
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# ================= SERIAL =================
SERIAL_PORT = "COM7"
BAUDRATE = 115200
ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

# ================= SPOTIFY SESSION =================
def get_spotify_volume():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and session.Process.name().lower() == "spotify.exe":
            return session._ctl.QueryInterface(ISimpleAudioVolume)
    return None

spotify_volume = get_spotify_volume()

print("Listening from ESP32...")

# ================= MAIN LOOP =================
while True:
    if ser.in_waiting:
        line = ser.readline().decode(errors="ignore").strip()
        print("RX:", line)

        # ---------- BUTTONS ----------
        if line == "BUTTON 1 PRESSED":
            keyboard.press_and_release("v")

        elif line == "BUTTON 2 PRESSED":
            keyboard.press_and_release("a")

        elif line == "BUTTON 3 PRESSED":
            keyboard.press_and_release("n")

        elif line == "BUTTON 4 PRESSED":
            keyboard.press_and_release("y")

        elif line == "BUTTON 5 PRESSED":
            keyboard.press_and_release("a")  # contoh

        # ---------- ENCODER 1 (SPOTIFY) ----------
        elif line == "ENC1 RIGHT":
            if spotify_volume:
                vol = spotify_volume.GetMasterVolume()
                spotify_volume.SetMasterVolume(min(vol + 0.01, 1.0), None)

        elif line == "ENC1 LEFT":
            if spotify_volume:
                vol = spotify_volume.GetMasterVolume()
                spotify_volume.SetMasterVolume(max(vol - 0.01, 0.0), None)

        elif line == "ENC1 BUTTON PRESSED":
            keyboard.send("play/pause media") # play / pause Spotify

        # ---------- ENCODER 2 (WINDOWS GLOBAL) ----------
        elif line == "ENC2 RIGHT":
            keyboard.send("volume up")

        elif line == "ENC2 LEFT":
            keyboard.send("volume down")

        elif line == "ENC2 BUTTON PRESSED":
            keyboard.send("volume mute")
   