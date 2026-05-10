ESP_KEYWORDS = (
    "esp32",
    "espressif",
    "usb jtag",
    "usb serial",
    "serial",
    "cp210",
    "ch340",
    "wch",
)


def _port_details(port) -> str:
    return " ".join(
        part.lower()
        for part in (port.description, port.manufacturer, port.product, port.hwid)
        if part
    )


def _score_port(port, preferred_port: str, expected_vid: int | None) -> int:
    score = 0
    details = _port_details(port)

    if preferred_port and port.device == preferred_port:
        score += 100
    if expected_vid is not None and getattr(port, "vid", None) == expected_vid:
        score += 50

    for keyword in ESP_KEYWORDS:
        if keyword in details:
            score += 10

    if "bluetooth" in details:
        score -= 20

    return score


def detect_best_port(list_ports_module, preferred_port: str = "", expected_vid: int | None = None) -> str:
    best_device = ""
    best_score = 0

    for port in list_ports_module.comports():
        score = _score_port(port, preferred_port, expected_vid)
        if score > best_score:
            best_score = score
            best_device = port.device

    return best_device
