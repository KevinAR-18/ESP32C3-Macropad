import argparse
import asyncio
from datetime import datetime

from bleak import BleakClient, BleakScanner

DEVICE_NAME = "KeyBloom-C3"
SERVICE_UUID = "7c3a0001-8f6e-4d4b-a8f3-6f8f9c1b0001"
EVENT_CHARACTERISTIC_UUID = "7c3a0002-8f6e-4d4b-a8f3-6f8f9c1b0001"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Test custom BLE notifications from the KeyBloom ESP32-C3."
    )
    parser.add_argument(
        "--address",
        help="Connect directly to a BLE address instead of scanning by name.",
    )
    parser.add_argument(
        "--scan-timeout",
        type=float,
        default=8.0,
        help="BLE scan timeout in seconds (default: 8).",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=3.0,
        help="Reconnect delay in seconds (default: 3).",
    )
    parser.add_argument(
        "--scan-only",
        action="store_true",
        help="List nearby BLE devices and exit without connecting.",
    )
    return parser.parse_args()


def now_text():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]


def notification_handler(_sender, data):
    event_text = bytes(data).decode("utf-8", errors="replace").strip()
    if event_text:
        print(f"[{now_text()}] [EVENT] {event_text}")


async def scan_devices(timeout):
    print(f"[BLE] Scanning for {timeout:g} seconds...")
    devices = await BleakScanner.discover(timeout=timeout, return_adv=True)

    for device, advertisement in devices.values():
        name = advertisement.local_name or device.name or "(unnamed)"
        service_uuids = {uuid.lower() for uuid in advertisement.service_uuids}
        marker = " <KeyBloom>" if SERVICE_UUID in service_uuids else ""
        print(f"[SCAN] {name} | {device.address} | RSSI {advertisement.rssi}{marker}")

    return devices


async def find_keybloom(timeout):
    devices = await scan_devices(timeout)
    for device, advertisement in devices.values():
        name = advertisement.local_name or device.name or ""
        service_uuids = {uuid.lower() for uuid in advertisement.service_uuids}
        if name == DEVICE_NAME or SERVICE_UUID in service_uuids:
            return device
    return None


async def monitor(address, scan_timeout, retry_delay):
    while True:
        disconnected = asyncio.Event()

        try:
            target = address or await find_keybloom(scan_timeout)
            if target is None:
                print(f"[BLE] {DEVICE_NAME} not found; retrying in {retry_delay:g}s.")
                await asyncio.sleep(retry_delay)
                continue

            target_label = target if isinstance(target, str) else target.address
            print(f"[BLE] Connecting to {target_label}...")

            def on_disconnect(_client):
                print("[BLE] Disconnected.")
                disconnected.set()

            async with BleakClient(target, disconnected_callback=on_disconnect) as client:
                print(f"[BLE] Connected: {client.is_connected}")
                await client.start_notify(EVENT_CHARACTERISTIC_UUID, notification_handler)
                initial_value = await client.read_gatt_char(EVENT_CHARACTERISTIC_UUID)
                notification_handler(None, initial_value)
                print("[BLE] Listening for events. Press Ctrl+C to stop.")
                await disconnected.wait()

        except asyncio.CancelledError:
            raise
        except Exception as error:
            print(f"[BLE] Connection error: {error}")

        print(f"[BLE] Reconnecting in {retry_delay:g}s...")
        await asyncio.sleep(retry_delay)


async def async_main(args):
    if args.scan_only:
        await scan_devices(args.scan_timeout)
        return
    await monitor(args.address, args.scan_timeout, args.retry_delay)


def main():
    args = parse_args()
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        print("\n[BLE] Test stopped.")


if __name__ == "__main__":
    main()
