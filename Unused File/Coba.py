import serial.tools.list_ports

def find_esp32_port():
    for port in serial.tools.list_ports.comports():
        vid = port.vid
        pid = port.pid

        # Espressif VID
        if vid == 0x303A:
            return port.device

    return None

port = find_esp32_port()

if not port:
    print("ESP32-C3 not found")
    exit(1)

print("ESP32 found on", port)
ser = serial.Serial(port, 115200, timeout=1)
