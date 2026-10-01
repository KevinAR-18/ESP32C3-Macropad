import asyncio
import time
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from PySide6.QtCore import QCoreApplication
from connection.manager import ConnectionManager, ConnectionWorker, normalize_settings

APP = QCoreApplication.instance() or QCoreApplication([])


class FakePort:
    def __init__(self, reply=True):
        self.port = "COM_TEST"
        self.reply = reply
        self.received = b""
        self.writes = []
        self.closed = False

    @property
    def in_waiting(self):
        return len(self.received)

    def open(self):
        pass

    def close(self):
        self.closed = True

    def read(self, count):
        data, self.received = self.received[:count], self.received[count:]
        return data

    def write(self, data):
        self.writes.append(data)
        if self.reply and data.startswith(b"KB HELLO "):
            self.received += data.replace(b"KB HELLO ", b"KB READY ")
        elif self.reply and data.startswith(b"KB PING "):
            self.received += data.replace(b"KB PING ", b"KB PONG ")
        return len(data)


class SerialTests(unittest.IsolatedAsyncioTestCase):
    def worker(self):
        return ConnectionWorker(normalize_settings({}), {"auto_detect": True})

    async def test_usb_requires_handshake_then_cancels_ble_and_routes_events(self):
        worker = self.worker()
        port = FakePort()
        worker.port = port
        worker.session = "test-session"
        worker.opened = time.monotonic()
        worker.ble_task = asyncio.create_task(asyncio.sleep(100))
        task = worker.ble_task
        events = []
        worker.event.connect(lambda *event: events.append(event))
        await worker.check_serial()
        self.assertTrue(worker.usb_ready)
        self.assertTrue(task.cancelled())
        self.assertIn(b"KB POWER 1 60 600\n", port.writes)
        port.received = b"BUTTON 1 PRES"
        await worker.check_serial()
        self.assertEqual(events, [])
        port.received = b"SED\nBUTTON 1 PRESSED\n"
        await worker.check_serial()
        self.assertEqual(len(events), 2)  # legitimate hold repeats are preserved
        worker.close_serial()
        self.assertIn(b"KB BYE test-session\n", port.writes)

    async def test_wrong_device_is_not_accepted_and_times_out(self):
        worker = self.worker()
        port = FakePort(reply=False)
        worker.port = port
        worker.session = "correct"
        worker.opened = time.monotonic() - 5
        port.received = b"KB READY wrong\nBUTTON 1 PRESSED\n"
        events = []
        worker.event.connect(lambda *event: events.append(event))
        await worker.check_serial()
        self.assertFalse(worker.usb_ready)
        self.assertTrue(port.closed)
        self.assertEqual(events, [])

    async def test_missing_heartbeat_releases_usb_for_ble(self):
        worker = self.worker()
        worker.port = FakePort(reply=False)
        worker.usb_ready = True
        worker.pong = time.monotonic() - 4
        await worker.check_serial()
        self.assertIsNone(worker.port)
        self.assertFalse(worker.usb_ready)
        self.assertEqual(worker.next_ble, 0)

    async def test_busy_port_does_not_prevent_next_candidate(self):
        worker = self.worker()
        candidates = [SimpleNamespace(device=name, description="esp32", manufacturer="", product="", hwid="")
                      for name in ("COM1", "COM2")]
        import serial
        with patch("connection.manager.list_ports.comports", return_value=candidates), \
             patch("connection.manager.serial.Serial", side_effect=[serial.SerialException("busy"), FakePort()]):
            await worker.check_serial()
        self.assertTrue(worker.usb_ready)
        worker.close_serial()


class PersistenceTests(unittest.TestCase):
    def test_only_successful_connection_is_saved(self):
        manager = ConnectionManager({}, {})
        manager.connect_device("AA")
        self.assertEqual(manager.settings["address"], "")
        manager._remember("AA", "KeyBloom-C3", manager.generation)
        self.assertEqual(manager.settings["address"], "AA")
        self.assertTrue(manager.settings["reconnect"])

    def test_disconnect_survives_reload_and_rejects_stale_success(self):
        manager = ConnectionManager({"address": "AA", "reconnect": True}, {})
        manager.connect_device("BB")
        generation = manager.generation
        manager.disconnect_device()
        manager._remember("BB", "Other", generation)
        self.assertEqual(manager.settings["address"], "AA")
        self.assertFalse(normalize_settings(manager.settings)["reconnect"])
        manager.disconnect_device(forget=True)
        self.assertEqual(manager.settings["address"], "")

    def test_queued_ble_event_rejected_after_manual_disconnect(self):
        manager = ConnectionManager({"address": "AA", "reconnect": True}, {})
        events = []
        manager.event.connect(events.append)
        generation = manager.generation
        manager.disconnect_device()
        manager._event("BLE", "BUTTON 1 PRESSED", generation)
        self.assertEqual(events, [])

    def test_power_settings_are_bounded_and_ordered(self):
        settings = normalize_settings({"idle_seconds": 9000, "sleep_seconds": "invalid"})
        self.assertEqual(settings["idle_seconds"], 3600)
        self.assertGreater(settings["sleep_seconds"], settings["idle_seconds"])


class BleTests(unittest.IsolatedAsyncioTestCase):
    async def test_subscribe_save_sleep_and_ignore_old_callback(self):
        worker = ConnectionWorker(normalize_settings({"address": "AA", "reconnect": True}), {})
        ready = asyncio.Event()
        class Client:
            services = SimpleNamespace(get_service=lambda uuid: object())
            def __init__(self, device, disconnected_callback):
                self.disconnect = disconnected_callback
            async def __aenter__(self):
                return self
            async def __aexit__(self, *args):
                self.disconnect(self)
            async def write_gatt_char(self, uuid, data, response):
                self.power = data
            async def start_notify(self, uuid, callback):
                self.notify = callback
                ready.set()
        async def find(*args, **kwargs):
            return SimpleNamespace(name="KeyBloom-C3", address="AA")
        saved, events = [], []
        worker.remembered.connect(lambda *args: saved.append(args))
        worker.event.connect(lambda *args: events.append(args))
        with patch("bleak.BleakScanner.find_device_by_address", side_effect=find), patch("bleak.BleakClient", Client):
            worker.ble_task = asyncio.create_task(worker.connect_ble("AA", worker.ble_epoch))
            await ready.wait()
            client = worker.client
            self.assertEqual(saved[0][0], "AA")
            self.assertEqual(client.power, b"KB POWER 1 60 600")
            client.notify(None, b"BUTTON 2 PRESSED")
            client.notify(None, b"KB SLEEP")
            self.assertTrue(worker.sleeping)
            self.assertEqual(len(events), 1)
            await worker.cancel_ble()
            client.notify(None, b"BUTTON 2 PRESSED")
            self.assertEqual(len(events), 1)

    async def test_failed_subscription_never_saves_device(self):
        worker = ConnectionWorker(normalize_settings({"address": "AA", "reconnect": True}), {})
        class Client:
            services = SimpleNamespace(get_service=lambda uuid: object())
            def __init__(self, *args, **kwargs):
                pass
            async def __aenter__(self):
                return self
            async def __aexit__(self, *args):
                pass
            async def write_gatt_char(self, *args, **kwargs):
                pass
            async def start_notify(self, *args):
                raise RuntimeError("Subscription failed")
        async def find(*args, **kwargs):
            return SimpleNamespace(name="KeyBloom-C3", address="AA")
        saved = []
        worker.remembered.connect(lambda *args: saved.append(args))
        with patch("bleak.BleakScanner.find_device_by_address", side_effect=find), patch("bleak.BleakClient", Client):
            await worker.connect_ble("AA", worker.ble_epoch)
        self.assertEqual(saved, [])
        self.assertIsNone(worker.client)
        self.assertGreater(worker.next_ble, time.monotonic())


if __name__ == "__main__":
    unittest.main()
