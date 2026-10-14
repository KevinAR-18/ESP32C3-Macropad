# KeyBloom v1.2.0

## Highlights

KeyBloom v1.2.0 adds system tray notifications for successful connections and reconnections, plus an easily accessible version label in the tray menu.

## New Features

- Tray notifications when a USB or saved Bluetooth Low Energy (BLE) device automatically connects.
- A distinct **Reconnected** notification when a previously connected device successfully connects again during the same app session.
- Successful manual BLE connections also show a connection notification.
- Connection notifications identify the USB COM port or Bluetooth device name and work while the app is minimized to the tray.
- A non-clickable **KeyBloom v1.2.0** label directly above **Exit** in the tray's right-click menu.

## Improvements and Updates

- Notifications are emitted only after a successful USB handshake or BLE notification subscription, not during searching or failed reconnect attempts.
- Repeated status updates do not generate duplicate connection notifications.
- Outdated BLE connection events are ignored after a manual disconnect or device selection change.
- The tray menu is ordered as **Show**, **Connection…**, a separator, the version label, and **Exit**.
- Updated the app version and build fallback version to **1.2.0**.

## Notes

- Tray notifications use the same native system notification mechanism as the existing minimize-to-tray notification. Their appearance, placement, and visibility depend on Windows notification settings, including Do Not Disturb.
- Reconnection history is tracked per device and transport for the current app session; the first automatic connection after restarting the app is shown as **Connected**.
- This update does not require firmware or saved-settings changes.
