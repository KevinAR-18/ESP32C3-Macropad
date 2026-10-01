#include <NimBLEDevice.h>
#include <Preferences.h>
#include <esp_sleep.h>
#include <esp_pm.h>
#include <driver/gpio.h>

// ESP32-C3 / NimBLE-Arduino 2.x. GPIO 5 is the ONLY deep-sleep wake button.
const uint8_t buttonPins[] = {0, 1, 2, 3, 4, 20, 5, 8};
const uint8_t encA[] = {6, 9};
const uint8_t encB[] = {7, 10};
const char *SERVICE_UUID = "7c3a0001-8f6e-4d4b-a8f3-6f8f9c1b0001";
const char *EVENT_UUID = "7c3a0002-8f6e-4d4b-a8f3-6f8f9c1b0001";
const char *CONTROL_UUID = "7c3a0003-8f6e-4d4b-a8f3-6f8f9c1b0001";
constexpr uint32_t DEBOUNCE_MS = 50, REPEAT_DELAY = 400, REPEAT_RATE = 80;
constexpr uint32_t USB_TIMEOUT = 3000;

struct Button {
  bool raw = HIGH, stable = HIGH;
  uint32_t changed = 0, pressed = 0, repeated = 0;
};
Button buttons[8];
int lastEncoderA[2];
bool suppressWakeClick = false;
uint32_t lastActivity = 0, lastHeartbeat = 0;
bool usbActive = false, idleMode = false, sleepEnabled = true;
uint32_t idleMs = 60000, sleepMs = 600000;
String serialLine, usbSession;
Preferences preferences;
NimBLEServer *bleServer = nullptr;
NimBLECharacteristic *events = nullptr;
volatile bool bleConnected = false;
volatile bool restartAdvertising = false, updateParams = false;
volatile uint16_t connectionHandle = BLE_HS_CONN_HANDLE_NONE;

// BLE callbacks run on another task. Transfer configuration through a bounded queue.
struct ControlMessage { char text[80]; };
QueueHandle_t controls;

class ServerCallbacks : public NimBLEServerCallbacks {
  void onConnect(NimBLEServer *, NimBLEConnInfo &info) override {
    connectionHandle = info.getConnHandle();
    bleConnected = true;
    updateParams = true;
  }
  void onDisconnect(NimBLEServer *, NimBLEConnInfo &, int) override {
    bleConnected = false;
    connectionHandle = BLE_HS_CONN_HANDLE_NONE;
    restartAdvertising = true;
  }
};

class ControlCallbacks : public NimBLECharacteristicCallbacks {
  void onWrite(NimBLECharacteristic *characteristic, NimBLEConnInfo &) override {
    auto value = characteristic->getValue();
    if (value.size() >= sizeof(ControlMessage::text)) return;
    ControlMessage message = {};
    memcpy(message.text, value.c_str(), value.size());
    xQueueSend(controls, &message, 0);
  }
};

void sendEvent(const String &text) {
  if (usbActive) {
    Serial.println(text);
  } else if (bleConnected) {
    events->setValue(text.c_str());
    events->notify();
  }
}

void setPowerConfig(const String &command) {
  unsigned int enabled, idleSeconds, sleepSeconds;
  char extra;
  if (sscanf(command.c_str(), "KB POWER %u %u %u %c", &enabled, &idleSeconds,
             &sleepSeconds, &extra) != 3) return;
  if (enabled > 1 || idleSeconds < 10 || idleSeconds > 3600 ||
      sleepSeconds <= idleSeconds || sleepSeconds > 86400) return;
  bool changed = sleepEnabled != bool(enabled) || idleMs != idleSeconds * 1000UL ||
                 sleepMs != sleepSeconds * 1000UL;
  sleepEnabled = enabled;
  idleMs = idleSeconds * 1000UL;
  sleepMs = sleepSeconds * 1000UL;
  if (changed) {
    preferences.putBool("enabled", sleepEnabled);
    preferences.putUInt("idle", idleMs);
    preferences.putUInt("sleep", sleepMs);
  }
}

void handleSerial() {
  // Limit work per pass so malformed traffic cannot starve physical input.
  for (int i = 0; i < 128 && Serial.available(); ++i) {
    char c = Serial.read();
    if (c == '\n') {
      serialLine.trim();
      if (serialLine.startsWith("KB HELLO ") && serialLine.length() <= 50) {
        usbSession = serialLine.substring(9);
        if (!usbSession.isEmpty()) {
          usbActive = true;
          lastHeartbeat = millis();
          Serial.println("KB READY " + usbSession);
        }
      } else if (usbActive && serialLine == "KB PING " + usbSession) {
        lastHeartbeat = millis();
        Serial.println("KB PONG " + usbSession);
      } else if (usbActive && serialLine == "KB BYE " + usbSession) {
        usbActive = false;
        lastActivity = millis();
      } else if (usbActive && serialLine.startsWith("KB POWER ")) {
        setPowerConfig(serialLine);
      }
      serialLine = "";
    } else if (c != '\r') {
      if (serialLine.length() < 79) serialLine += c;
      else serialLine = "";
    }
  }
  if (usbActive && millis() - lastHeartbeat >= USB_TIMEOUT) {
    usbActive = false;
    // Allow a full reconnect window after cable removal.
    lastActivity = millis();
  }
}

void setupBle() {
  NimBLEDevice::init("KeyBloom-C3");
  bleServer = NimBLEDevice::createServer();
  bleServer->setCallbacks(new ServerCallbacks());
  auto service = bleServer->createService(SERVICE_UUID);
  events = service->createCharacteristic(EVENT_UUID, NIMBLE_PROPERTY::READ | NIMBLE_PROPERTY::NOTIFY);
  events->setValue("START");
  auto control = service->createCharacteristic(CONTROL_UUID, NIMBLE_PROPERTY::WRITE);
  control->setCallbacks(new ControlCallbacks());
  service->start();
  auto advertising = NimBLEDevice::getAdvertising();
  advertising->addServiceUUID(SERVICE_UUID);
  advertising->setName("KeyBloom-C3");
  advertising->enableScanResponse(true);
  advertising->setMinInterval(160); // 100–200 ms during discovery
  advertising->setMaxInterval(320);
  advertising->start();
}

void emitButton(int index) {
  if (index < 6) sendEvent("BUTTON " + String(index + 1) + " PRESSED");
  else sendEvent("ENC" + String(index - 5) + " BUTTON PRESSED");
}

void handleInputs() {
  uint32_t now = millis();
  for (int i = 0; i < 8; ++i) {
    bool raw = digitalRead(buttonPins[i]);
    auto &b = buttons[i];
    if (raw != b.raw) {
      b.raw = raw;
      b.changed = now;
      lastActivity = now;
    }
    // Consume the entire wake click, including contact bounce and hold repeats.
    if (i == 6 && suppressWakeClick) {
      b.stable = raw;
      if (raw == HIGH && now - b.changed >= DEBOUNCE_MS) suppressWakeClick = false;
      continue;
    }
    if (raw != b.stable && now - b.changed >= DEBOUNCE_MS) {
      b.stable = raw;
      if (raw == LOW) {
        b.pressed = b.repeated = now;
        emitButton(i);
      }
    } else if (b.stable == LOW && raw == LOW && now - b.pressed >= REPEAT_DELAY &&
               now - b.repeated >= REPEAT_RATE) {
      emitButton(i);
      b.repeated = now;
    }
    if (raw == LOW) lastActivity = now;
  }
  for (int i = 0; i < 2; ++i) {
    int a = digitalRead(encA[i]);
    if (a != lastEncoderA[i]) {
      lastActivity = now;
      sendEvent("ENC" + String(i + 1) + (digitalRead(encB[i]) != a ? " LEFT" : " RIGHT"));
      lastEncoderA[i] = a;
    }
  }
}

void handlePower() {
  uint32_t elapsed = millis() - lastActivity;
  bool idle = !usbActive && elapsed >= idleMs;
  if (idle != idleMode || updateParams) {
    updateParams = false;
    idleMode = idle;
#if !defined(CONFIG_PM_ENABLE) || !CONFIG_PM_ENABLE
    // Stock Arduino builds usually disable dynamic power management. 80 MHz
    // keeps the BLE controller supported while reducing idle CPU consumption.
    setCpuFrequencyMhz(idle ? 80 : 160);
#endif
    if (bleConnected) {
      // Units: interval 1.25 ms, timeout 10 ms. Central may negotiate differently.
      bleServer->updateConnParams(connectionHandle, idle ? 80 : 12,
                                 idle ? 160 : 24, idle ? 4 : 0, 600);
    }
    auto advertising = NimBLEDevice::getAdvertising();
    if (!bleConnected) advertising->stop();
    advertising->setMinInterval(idle ? 1600 : 160);
    advertising->setMaxInterval(idle ? 2400 : 320);
    if (!bleConnected) advertising->start();
  }
  if (restartAdvertising) {
    restartAdvertising = false;
    NimBLEDevice::startAdvertising();
  }
  if (!usbActive && sleepEnabled && elapsed >= sleepMs) {
    for (auto pin : buttonPins) if (digitalRead(pin) == LOW) return;
    sendEvent("KB SLEEP");
    delay(100); // Allow the sleep notification to leave before shutting down BLE.
    NimBLEDevice::deinit(true);
    // C3 deep-sleep GPIO wake supports GPIO 0–5 only; encoder 1 switch is GPIO 5.
    esp_deep_sleep_enable_gpio_wakeup(1ULL << 5, ESP_GPIO_WAKEUP_GPIO_LOW);
    gpio_pullup_en(GPIO_NUM_5);
    gpio_pulldown_dis(GPIO_NUM_5);
    esp_deep_sleep_start();
  }
}

void setup() {
  Serial.begin(115200);
  serialLine.reserve(80);
  controls = xQueueCreate(4, sizeof(ControlMessage));
  preferences.begin("keybloom", false);
  sleepEnabled = preferences.getBool("enabled", true);
  idleMs = preferences.getUInt("idle", 60000);
  sleepMs = preferences.getUInt("sleep", 600000);
  if (idleMs < 10000 || idleMs > 3600000 || sleepMs <= idleMs || sleepMs > 86400000) {
    idleMs = 60000;
    sleepMs = 600000;
  }
  for (auto pin : buttonPins) pinMode(pin, INPUT_PULLUP);
  for (int i = 0; i < 2; ++i) {
    pinMode(encA[i], INPUT_PULLUP);
    pinMode(encB[i], INPUT_PULLUP);
    lastEncoderA[i] = digitalRead(encA[i]);
  }
  suppressWakeClick = esp_sleep_get_wakeup_cause() == ESP_SLEEP_WAKEUP_GPIO;
  // PM depends on the Arduino core build. Never force manual light-sleep with BLE.
#if defined(CONFIG_PM_ENABLE) && CONFIG_PM_ENABLE
  esp_pm_config_t pm = {};
  pm.max_freq_mhz = 160;
  pm.min_freq_mhz = 40;
#if defined(CONFIG_FREERTOS_USE_TICKLESS_IDLE) && CONFIG_FREERTOS_USE_TICKLESS_IDLE && defined(CONFIG_BT_CTRL_MODEM_SLEEP) && CONFIG_BT_CTRL_MODEM_SLEEP
  pm.light_sleep_enable = true;
#endif
  esp_pm_configure(&pm);
#endif
  setupBle();
  lastActivity = millis();
}

void loop() {
  handleSerial();
  ControlMessage message;
  if (xQueueReceive(controls, &message, 0) == pdTRUE) setPowerConfig(String(message.text));
  handleInputs();
  handlePower();
  // Yield to the RTOS/BLE tasks without slowing encoder polling in idle mode.
  delay(1);
}
