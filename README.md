# KeyBloom

KeyBloom is a Windows desktop companion for a custom ESP32-C3 macro pad. It provides a PySide6-based interface to configure multiple profiles, map each hardware button to a keyboard shortcut or application launcher, and keep the app running in the system tray while listening to serial events from the device.

## Features

- 5 configurable profiles
- 6 slots per profile
- Keyboard shortcut capture with presets
- Media key capture support, including fallback for `Fn`-based media keys
- Application launcher per slot
- ESP32 serial auto-detection with reconnect retry/backoff
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
- [utils/date_utils.py](./utils/date_utils.py): clock/date formatting helper
- [resources.qrc](./resources.qrc): Qt resource manifest
- [resources_rc.py](./resources_rc.py): generated Qt resource module
- [build.bat](./build.bat): main PyInstaller build script
- [KeyBloom.spec](./KeyBloom.spec): PyInstaller spec file
- [examplebuildbat.bat](./examplebuildbat.bat): simplified build example
- [PCB_Macropad/Macropad_PCB](./PCB_Macropad/Macropad_PCB): KiCad project for the macro pad PCB
- [ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino](./ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino): ESP32-C3 firmware source

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
