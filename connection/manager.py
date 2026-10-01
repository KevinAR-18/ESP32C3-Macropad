"""One background event loop owns both transports; Qt only receives ordered events."""
import asyncio
import queue
import secrets
import time

import serial
from serial.tools import list_ports
from PySide6.QtCore import QObject, QThread, Signal

from serial_tools.port_detector import _score_port

SERVICE_UUID = "7c3a0001-8f6e-4d4b-a8f3-6f8f9c1b0001"
EVENT_UUID = "7c3a0002-8f6e-4d4b-a8f3-6f8f9c1b0001"
CONTROL_UUID = "7c3a0003-8f6e-4d4b-a8f3-6f8f9c1b0001"


def normalize_settings(value):
    value = value if isinstance(value, dict) else {}
    def bounded(key, default, minimum, maximum):
        try:
            return max(minimum, min(maximum, int(value.get(key, default))))
        except (ValueError, TypeError):
            return default
    idle = bounded("idle_seconds", 60, 10, 3600)
    return {
        "address": str(value.get("address", "")),
        "name": str(value.get("name", "KeyBloom-C3")),
        "reconnect": bool(value.get("reconnect", False)),
        "auto_sleep": bool(value.get("auto_sleep", True)),
        "idle_seconds": idle,
        "sleep_seconds": max(idle + 1, bounded("sleep_seconds", 600, 11, 86400)),
    }


class ConnectionWorker(QThread):
    event = Signal(str, str, int)  # transport, payload, user selection generation
    status = Signal(str)
    devices = Signal(object)
    remembered = Signal(str, str, int)

    def __init__(self, settings, serial_settings, parent=None):
        super().__init__(parent)
        self.commands = queue.Queue()
        self.settings = dict(settings)
        self.serial_settings = dict(serial_settings)
        self.stopping = False
        self.port = None
        self.usb_ready = False
        self.buffer = b""
        self.session = ""
        self.opened = self.pong = self.ping = 0
        self.next_usb = 0
        self.failed_ports = {}
        self.ble_task = self.scan_task = None
        self.client = None
        self.ble_epoch = 0
        self.next_ble = 0
        self.retry = 2
        self.sleeping = False
        self.last_status = ""
        self.generation = 0

    def report(self, text):
        if text != self.last_status:
            self.last_status = text
            self.status.emit(text)

    def run(self):
        asyncio.run(self.monitor())

    def power_command(self):
        s = self.settings
        return f"KB POWER {int(s['auto_sleep'])} {s['idle_seconds']} {s['sleep_seconds']}"

    def write_serial(self, text):
        self.port.write((text + "\n").encode("ascii"))

    def close_serial(self):
        if self.port:
            try:
                if self.usb_ready:
                    self.write_serial("KB BYE " + self.session)
                self.port.close()
            except (serial.SerialException, OSError):
                pass
        self.port = None
        self.usb_ready = False
        self.buffer = b""

    async def cancel_ble(self):
        self.ble_epoch += 1
        if self.ble_task:
            self.ble_task.cancel()
            await asyncio.gather(self.ble_task, return_exceptions=True)
            self.ble_task = None
        self.client = None

    async def scan(self):
        try:
            from bleak import BleakScanner
            results = await BleakScanner.discover(timeout=5, return_adv=True)
            devices = []
            for device, adv in results.values():
                if SERVICE_UUID in [u.lower() for u in adv.service_uuids]:
                    devices.append((device.address, adv.local_name or device.name or "KeyBloom-C3"))
            self.devices.emit(devices)
            if not self.usb_ready and not self.client:
                self.report(f"Scan complete — {len(devices)} device(s)")
        except Exception as error:
            self.devices.emit([])
            if not self.usb_ready:
                self.report(f"Bluetooth scan unavailable: {error}")

    async def connect_ble(self, address, epoch):
        try:
            from bleak import BleakClient, BleakScanner
            if not self.sleeping:
                self.report("BLE searching / reconnecting…")
            device = await BleakScanner.find_device_by_address(address, timeout=5)
            if device is None:
                raise RuntimeError("Saved device not found; click encoder 1 if sleeping")
            disconnected = asyncio.Event()
            async with BleakClient(device, disconnected_callback=lambda _: disconnected.set()) as client:
                if client.services.get_service(SERVICE_UUID) is None:
                    raise RuntimeError("Device is not a KeyBloom service")
                # Production firmware includes control characteristic; reject old test firmware.
                await client.write_gatt_char(CONTROL_UUID, self.power_command().encode(), response=True)
                def notification(_, data):
                    if epoch != self.ble_epoch or self.usb_ready or not self.client:
                        return
                    text = bytes(data).decode("utf-8", errors="replace").strip()
                    if text == "KB SLEEP":
                        self.sleeping = True
                        self.report("Sleeping — click encoder 1 to wake")
                    elif len(text) <= 80:
                        self.event.emit("BLE", text, self.generation)
                await client.start_notify(EVENT_UUID, notification)
                if epoch != self.ble_epoch or self.usb_ready:
                    return
                self.client = client
                self.sleeping = False
                self.retry = 2
                name = device.name or self.settings["name"]
                self.remembered.emit(address, name, self.generation)
                self.report(f"BLE Connected — {name}")
                await disconnected.wait()
        except asyncio.CancelledError:
            raise
        except Exception as error:
            if not self.usb_ready and not self.sleeping:
                self.report(f"BLE unavailable / reconnecting: {error}")
        finally:
            self.client = None
            self.next_ble = time.monotonic() + self.retry
            self.retry = min(30, self.retry * 2)
            if not self.stopping and not self.usb_ready and self.sleeping:
                self.report("Sleeping — click encoder 1 to wake")

    async def check_serial(self):
        now = time.monotonic()
        try:
            if self.port is None and now >= self.next_usb:
                self.next_usb = now + 2
                preferred = self.serial_settings.get("port", "")
                candidates = list(list_ports.comports())
                if self.serial_settings.get("auto_detect", True):
                    candidates = [p for p in candidates if _score_port(p, preferred, None) > 0]
                    candidates.sort(key=lambda p: _score_port(p, preferred, None), reverse=True)
                else:
                    candidates = [p for p in candidates if p.device == preferred]
                for candidate in candidates:
                    if self.failed_ports.get(candidate.device, 0) > now:
                        continue
                    self.failed_ports[candidate.device] = now + 15
                    try:
                        port = serial.Serial()
                        port.port = candidate.device
                        port.baudrate = 115200
                        port.timeout = 0
                        port.write_timeout = 0.2
                        port.dtr = True  # Native USB CDC must see a listening host.
                        port.rts = False
                        port.open()
                        self.port = port
                        self.session = secrets.token_hex(8)
                        self.opened = now
                        self.ping = 0
                        break
                    except (serial.SerialException, OSError):
                        continue
            if self.port is None:
                return
            if now - self.ping >= 1:
                self.write_serial(("KB PING " if self.usb_ready else "KB HELLO ") + self.session)
                self.ping = now
            chunk = self.port.read(min(self.port.in_waiting, 4096))
            self.buffer += chunk
            if len(self.buffer) > 8192:
                raise RuntimeError("Serial buffer exceeded")
            while b"\n" in self.buffer:
                line, self.buffer = self.buffer.split(b"\n", 1)
                text = line.decode("utf-8", errors="replace").strip()
                if text == "KB READY " + self.session and not self.usb_ready:
                    self.usb_ready = True
                    self.pong = now
                    self.write_serial(self.power_command())
                    await self.cancel_ble()
                    self.report(f"USB Connected — {self.port.port}")
                elif text == "KB PONG " + self.session:
                    self.pong = now
                elif self.usb_ready and not text.startswith("KB "):
                    self.event.emit("USB", text, self.generation)
            if (not self.usb_ready and now - self.opened > 4) or (self.usb_ready and now - self.pong > 3):
                raise RuntimeError("USB handshake/heartbeat timeout")
        except (serial.SerialException, OSError, RuntimeError) as error:
            was_ready = self.usb_ready
            self.close_serial()
            if was_ready:
                self.next_ble = 0
                self.report(f"USB disconnected — {error}")

    async def monitor(self):
        self.report("Searching for USB / saved BLE device…")
        try:
            while not self.stopping:
                while not self.commands.empty():
                    command, payload = self.commands.get_nowait()
                    if command == "stop":
                        self.stopping = True
                        break
                    if command == "scan":
                        if self.scan_task is None or self.scan_task.done():
                            if not self.client:
                                await self.cancel_ble()
                            self.scan_task = asyncio.create_task(self.scan())
                    elif command == "serial":
                        self.close_serial()
                        self.serial_settings = payload
                        self.next_usb = 0
                        self.failed_ports.clear()
                    elif command == "settings":
                        payload, generation = payload
                        self.settings = payload
                        if generation != self.generation:
                            await self.cancel_ble()
                            self.generation = generation
                            self.sleeping = False
                            self.next_ble = 0
                            self.retry = 2
                        try:
                            if self.usb_ready:
                                self.write_serial(self.power_command())
                            elif self.client:
                                await self.client.write_gatt_char(CONTROL_UUID, self.power_command().encode(), response=True)
                        except Exception as error:
                            self.report(f"Power settings pending reconnect: {error}")
                        if not payload["reconnect"] and not self.usb_ready:
                            self.report("BLE disconnected manually" if payload["address"] else "No saved BLE device — Scan to connect")
                if self.stopping:
                    break
                await self.check_serial()
                if (not self.usb_ready and self.settings["reconnect"] and self.settings["address"]
                        and time.monotonic() >= self.next_ble
                        and (self.scan_task is None or self.scan_task.done())
                        and (self.ble_task is None or self.ble_task.done())):
                    self.ble_task = asyncio.create_task(self.connect_ble(self.settings["address"], self.ble_epoch))
                await asyncio.sleep(0.01 if self.port else 0.1)
        finally:
            self.stopping = True
            self.close_serial()
            await self.cancel_ble()
            if self.scan_task:
                self.scan_task.cancel()
                await asyncio.gather(self.scan_task, return_exceptions=True)


class ConnectionManager(QObject):
    event = Signal(str)
    status = Signal(str)
    devices = Signal(object)
    changed = Signal()

    def __init__(self, settings, serial_settings, parent=None):
        super().__init__(parent)
        self.settings = normalize_settings(settings)
        self.pending_address = ""
        self.generation = 0
        self.worker = ConnectionWorker(self.settings, serial_settings, self)
        self.worker.event.connect(self._event)
        self.worker.status.connect(self.status)
        self.worker.devices.connect(self.devices)
        self.worker.remembered.connect(self._remember)

    def _event(self, transport, text, generation):
        if transport == "USB" or (generation == self.generation and (self.settings["reconnect"] or self.pending_address)):
            self.event.emit(text)

    def _remember(self, address, name, generation):
        if generation != self.generation:
            return
        if address != self.pending_address and not (address == self.settings["address"] and self.settings["reconnect"]):
            return
        self.settings.update(address=address, name=name, reconnect=True)
        self.pending_address = ""
        self.changed.emit()

    def send_settings(self):
        settings = dict(self.settings)
        if self.pending_address:
            settings.update(address=self.pending_address, reconnect=True)
        self.worker.commands.put(("settings", (settings, self.generation)))

    def connect_device(self, address):
        if address:
            self.generation += 1
            self.pending_address = address
            self.send_settings()

    def disconnect_device(self, forget=False):
        self.generation += 1
        self.pending_address = ""
        self.settings["reconnect"] = False
        if forget:
            self.settings.update(address="", name="KeyBloom-C3")
        self.send_settings()
        self.changed.emit()

    def stop(self):
        self.worker.commands.put(("stop", None))
        self.worker.wait()
