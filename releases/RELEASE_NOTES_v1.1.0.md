# KeyBloom v1.1.0

## Highlights

KeyBloom v1.1.0 introduces more reliable USB and Bluetooth Low Energy (BLE) connectivity, connection and power-saving controls, and flexible per-profile action mappings for buttons and rotary encoders.

## New Features

- USB and BLE connectivity support in the KeyBloom app.
- USB connection priority to keep input responsive when a data cable is connected.
- Automatic USB detection or manual COM port selection with device handshake validation.
- A new connection dialog available from **Settings > USB / Bluetooth Connection...** or the tray menu's **Connection...** item.
- Scan, select, connect, disconnect, and forget BLE devices directly from the app.
- Successfully connected BLE devices can be saved and automatically reconnected when the app starts or a connection is lost.
- Production USB and BLE communication protocol:
  - `KB HELLO` and `KB READY` handshake.
  - `KB PING` and `KB PONG` heartbeat.
  - Clean connection release through `KB BYE`.
- ESP32-C3 firmware support for power-saving settings sent by the app.
- Reduced idle power usage, including CPU clock reduction when supported.
- Configurable deep sleep after a period of inactivity.
- Wake from deep sleep by clicking encoder 1 on GPIO 5.
- The device can report its sleep status to the app through the `KB SLEEP` notification.
- Per-profile action mapping for all six buttons and both rotary encoders.
- A dedicated action editor for assigning keyboard shortcuts, media controls, audio controls, applications, files, folders, URLs, text, or profile switching.
- Rotary encoder actions can be configured independently for left, right, and click events, including Spotify volume controls.
- Import and export action mappings, copy an action, and copy mappings from another profile.

## Improvements and Updates

- USB and BLE connection handling has been moved into a connection manager for a clearer, more maintainable structure.
- BLE reconnect uses backoff to avoid unnecessary repeated scans.
- Connection and power-saving settings are stored in the app configuration.
- Settings, shortcuts, serial ports, and UI components have been organized into a clearer module structure.
- Shortcut normalization and media key handling have been improved.
- The build script reads the app version and displays version information for the generated build.
- USB/BLE transport policy tests and a UI smoke test have been added.
- Firmware, BLE, connection protocol, and sleep/wake documentation has been updated.
- Button and rotary action mappings are persisted per profile, with defaults retained for existing rotary behavior.
- The action-mapping editor includes validation and a preview-friendly workflow for assigning actions.
- The main interface provides a dedicated **Edit Rotary Actions** entry point; button mappings remain available from each button slot's context menu.
- Action mapping and dispatch tests have been added for custom button and rotary assignments.

## Important Before Updating

- Update both the desktop app **and** ESP32-C3 firmware together. Older serial firmware and the prototype BLE firmware do not support the v1.1.0 production handshake and control protocol.
- The main firmware is located at `ProgramESP32C3_Macropad/ProgramESP32C3_Macropad.ino`.
- The firmware requires **NimBLE-Arduino 2.x**. It was compiled with Arduino-ESP32 **3.3.10** using the `esp32:esp32:esp32c3:CDCOnBoot=cdc` target.
- For BLE, use the KeyBloom connection dialog. Do not pair the device through Windows Bluetooth settings.
- The app cannot wake a device already in deep sleep. Click encoder 1 first to wake the device.
- The USB cable must support data to be used as a KeyBloom USB connection.
- Button-action and rotary-action exports use different formats: `keybloom-actions-v1` and `keybloom-rotary-actions-v1`. Import each file through its corresponding editor.

## Verification Notes

- Connection tests, a UI smoke test, and action mapping/dispatch tests have been added to the repository.
- In the environment used to prepare these release notes, `pytest -q` could not collect tests because the `bleak` dependency was not installed and module resolution for `connection` was not configured for that command.
- Perform hardware testing before daily use: measure power consumption in active/idle/deep-sleep states, test encoder 1 wake, BLE reconnect, and USB hot-plug behavior.

## Upgrade Steps

1. Download and run the KeyBloom v1.1.0 build.
2. Upload the latest `ProgramESP32C3_Macropad.ino` firmware to the ESP32-C3.
3. Open KeyBloom, then select **Settings > USB / Bluetooth Connection...**.
4. Connect the device by USB, or scan for BLE devices, select `KeyBloom-C3`, then click **Connect**.
