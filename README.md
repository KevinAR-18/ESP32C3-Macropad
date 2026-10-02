# KeyBloom

KeyBloom is a Windows desktop companion for a custom ESP32-C3 macro pad. It provides a PySide6-based interface to configure multiple profiles, map each hardware button to a keyboard shortcut or application launcher, and keep the app running in the system tray while listening to serial events from the device.

## Features

- 5 configurable profiles
- 6 slots per profile
- Keyboard shortcut capture with presets
- Media key capture support, including fallback for `Fn`-based media keys
- Application launcher per slot
- ESP32 serial auto-detection with reconnect retry/backoff
- USB-priority transport with verified handshake and heartbeat
- BLE scan/connect/disconnect/forget inside KeyBloom, with saved-device reconnect
- BLE idle power reduction and encoder-1-only deep-sleep wake
- System tray mode for background runtime
- Windows startup integration with start-minimized tray behavior
- Default startup page always returns to Profile 1
- Settings stored in `%APPDATA%\KeyBloom\settings.json`
- Spotify session volume control for the second encoder
- KiCad PCB files included in the repository
- ESP32-C3 firmware source included in the repository

## Project Structure

- [main.py](./main.py): application entry point and main runtime logic
- [keybloom.ui](./keybloom.ui): Qt Designer source file
- [ui/ui_keybloom.py](./ui/ui_keybloom.py): generated Qt UI file
- [ui/preview_button.py](./ui/preview_button.py): custom keycap preview widget
- [ui/ui_functions.py](./ui/ui_functions.py): borderless window and drag helpers
- [config/settings_manager.py](./config/settings_manager.py): settings load/save and profile serialization
- [input/key_capture.py](./input/key_capture.py): shortcut capture event filter
- [input/shortcut_utils.py](./input/shortcut_utils.py): shortcut normalization helpers
- [serial_tools/port_detector.py](./serial_tools/port_detector.py): serial port auto-detection helpers
- [connection/manager.py](./connection/manager.py): background USB/BLE transport and connection policy
- [connection/dialog.py](./connection/dialog.py): connection and power settings dialog
- [utils/date_utils.py](./utils/date_utils.py): clock/date formatting helper
- [resources.qrc](./resources.qrc): Qt resource manifest
- [resources_rc.py](./resources_rc.py): generated Qt resource module
- [build.bat](./build.bat): main PyInstaller build script
- [KeyBloom.spec](./KeyBloom.spec): PyInstaller spec file
- [examplebuildbat.bat](./examplebuildbat.bat): simplified build example
- [PCB_Macropad/Macropad_PCB](./PCB_Macropad/Macropad_PCB): KiCad project for the macro pad PCB
- [ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino](./ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino): ESP32-C3 firmware source
- [bluetooth_test](./bluetooth_test): isolated ESP32-C3 BLE communication prototype for Windows 11

## Requirements

- Windows
- Python 3.12+ recommended
- A virtual environment in `.venv`
- ESP32-C3 macro pad firmware that sends serial messages compatible with the app

Install dependencies:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Running From Source

```powershell
.venv\Scripts\python.exe main.py
```

## Runtime Behavior

- When Auto Startup is enabled, Windows launches KeyBloom with a start-minimized flag so the app goes directly to the system tray.
- When the main window is opened manually, the app always starts on Profile 1.
- Shortcut capture uses the Qt event path first and temporarily enables a global keyboard hook while recording, which improves capture for media keys such as `Media Next` and `Media Previous`.
- Serial auto-detect keeps retrying with a reconnect backoff when the ESP32-C3 disconnects or re-enumerates.

## Settings Location

At runtime, the app saves settings to:

```text
%APPDATA%\KeyBloom\settings.json
```

Legacy settings next to the executable or project folder are still readable as fallback.

## Build EXE

Install PyInstaller first:

```powershell
.venv\Scripts\python.exe -m pip install pyinstaller
```

Then run:

```powershell
build.bat
```

Expected output:

```text
dist\KeyBloom.exe
dist\icon.ico
```

`build.bat` also copies `icon.ico` into `dist\` after a successful build.

## Hardware Files

The repository also includes the hardware design files for the macro pad PCB.

- The KiCad project is located in [PCB_Macropad/Macropad_PCB](./PCB_Macropad/Macropad_PCB).
- The PCB design files are already prepared for production and intended for JLCPCB workflow.
- The project includes the schematic, PCB layout, and backup archives generated during board iteration.

## ESP32-C3 Firmware

### Dual USB/BLE setup

Upload `ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino` with
**NimBLE-Arduino 2.x** installed. Compilation has been checked with Arduino-ESP32
**3.3.10**, target `esp32:esp32:esp32c3:CDCOnBoot=cdc` (native USB CDC enabled).
Choose the board/USB settings matching your actual hardware. Close Serial Monitor
before connecting KeyBloom. Update both desktop app and firmware together: the old
serial firmware and BLE test firmware do not implement the production handshake/control protocol.

Open **Settings → USB / Bluetooth Connection…**, or **Connection…** in the tray menu.

1. For USB, enable Auto Detect (or enter the COM port manually). KeyBloom verifies
   the device before selecting USB. An open COM port alone is not sufficient.
2. For BLE, click **Scan**, select `KeyBloom-C3`, then **Connect**. Use the KeyBloom
   dialog rather than Windows Bluetooth pairing. The device is saved only after
   the BLE service, control write, and event subscription succeed.
3. Saved devices reconnect on app startup and after an unexpected disconnection.
4. **Disconnect** keeps the device saved and disables reconnect, including after
   an app restart. **Connect** enables it again. **Forget device** removes the saved device.
5. USB takes priority. Removing USB permits BLE reconnect unless manually disconnected.
   A charging cable without an active KeyBloom data connection does not select USB.

The board needs battery/another power source to keep running when USB is removed.
The prototype BLE client must be closed before connecting the desktop app.

### Custom button and rotary actions

- On any profile page, click **Edit button & rotary actions…** or click a button
  preview and choose **Edit Action…**.
- Each profile has 12 mappings: six buttons and left/right/click for each rotary.
- Available actions: keyboard shortcut, media (play/pause, next, previous, stop),
  system audio, Spotify volume, open app/file/folder, URL, text, switch profile,
  and None. Spotify volume steps can be set from 1% to 100%.
- Text preserves whitespace and is typed into the focused application. Media
  controls use the Windows media session; they are not Spotify-specific.
- **Copy/Paste** copies one mapping. The profile selector copies all 12 mappings
  from another profile. **Export/Import profile** uses a portable JSON file.
  Imported/copied changes take effect only after **Save**; Cancel discards them.
- Mappings are saved in the application's settings and restored on restart.
  Existing button mappings and the original rotary defaults are retained.
- Firmware currently repeats held buttons; briefly press toggle actions such
  as Play/Pause and profile switching. Long/double press are not available yet.

### Power and wake-up behavior

- Default: after **60 seconds** of physical inactivity, request longer BLE connection
  intervals/slave latency and slower advertising when disconnected. The central
  (Windows) can negotiate different connection parameters.
- Stock Arduino-ESP32 3.3.10 in this environment has `CONFIG_PM_ENABLE` and
  `CONFIG_BT_CTRL_MODEM_SLEEP` disabled. This build reduces CPU speed to **80 MHz**
  while idle and restores **160 MHz** on activity/USB. It does **not** claim connected
  automatic light-sleep. Custom cores with compatible PM/modem-sleep/tickless-idle
  support can use the guarded PM configuration in the sketch.
- Default: after **600 seconds**, enter deep sleep and disconnect BLE. This also
  applies when advertising without a connected client. Active USB heartbeat prevents sleep.
- **Only clicking encoder 1 (GPIO 5) wakes from deep sleep.** Rotation and other
  buttons do not wake it. The complete wake click, including hold/repeat, is consumed;
  release it before using encoder 1 again.
- KeyBloom reconnects to a waking saved device unless Disconnect was selected.
  A sleeping board cannot be woken by the app's Connect button. Click encoder 1 first.
- USB plug-in wake depends on the board's power/reset wiring; do not assume it wakes
  an already battery-powered sleeping board. Use encoder 1 if needed.
- Change timings or disable deep sleep with **Save power settings**. Settings are saved
  in AppData and sent on connection; firmware persists changed power settings in NVS.
- Sleep status is shown when the firmware's notification reaches the app. A silent
  disconnect cannot reliably be identified as sleep. Reconnect scanning backs off to 30 seconds.

Hardware verification is still required: measure board current in active/idle/deep-sleep
states, confirm GPIO 5 remains pulled high when released, exercise wake/reconnect and
USB hot-plug, and check that LED/regulator consumption meets your battery-life needs.
Do not infer battery life from firmware sleep mode alone.

### Protocol and validation

BLE name/service/event UUID remain compatible with the prototype. Production adds
the writable control characteristic `7c3a0003-8f6e-4d4b-a8f3-6f8f9c1b0001`.

- USB: `KB HELLO <session>` → `KB READY <session>`.
- Heartbeat every second: `KB PING <session>` → `KB PONG <session>`; 3-second lease.
- Graceful release: `KB BYE <session>`.
- Power configuration: `KB POWER <0|1> <idle_seconds> <sleep_seconds>` over USB or BLE.
- Before deep sleep: BLE notification `KB SLEEP` (best effort).

Run desktop policy tests and the isolated UI smoke check:

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
.venv\Scripts\python.exe tests\smoke_ui.py
```

The ESP32-C3 firmware is already included in the repository:

- Firmware source: [ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino](./ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino)
- The desktop app expects the board firmware to send serial messages that match the event format documented below.

## Serial Event Format

The app currently reacts to messages such as:

```text
BUTTON 1 PRESSED
ENC1 RIGHT
ENC1 LEFT
ENC1 BUTTON PRESSED
ENC2 RIGHT
ENC2 LEFT
ENC2 BUTTON PRESSED
START
```

## Notes

- The UI is generated from `keybloom.ui`, but runtime optimizations are handled in Python code.
- The app is tuned to stay lighter while minimized to tray by reducing unnecessary timers, delayed widget setup, and lazy-loading heavy modules.
- `requirements.txt` is kept intentionally small to match the runtime dependencies used by the current app.
