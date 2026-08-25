#include <NimBLEDevice.h>

// Use the same pins and event text as the production serial firmware so this
// prototype can later share KeyBloom's existing event handler.
const int buttonPins[6] = {0, 1, 2, 3, 4, 20};
const int buttonCount = sizeof(buttonPins) / sizeof(buttonPins[0]);

#define ENC1_A 6
#define ENC1_B 7
#define ENC1_SW 5

#define ENC2_SW 8
#define ENC2_A 9
#define ENC2_B 10

#define DEBOUNCE_TIME 50
#define REPEAT_DELAY 400
#define REPEAT_RATE 80

const char *DEVICE_NAME = "KeyBloom-C3";
const char *SERVICE_UUID = "7c3a0001-8f6e-4d4b-a8f3-6f8f9c1b0001";
const char *EVENT_CHARACTERISTIC_UUID = "7c3a0002-8f6e-4d4b-a8f3-6f8f9c1b0001";

NimBLECharacteristic *eventCharacteristic = nullptr;
volatile bool bleConnected = false;

bool lastButtonState[buttonCount] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};
unsigned long pressTime[buttonCount] = {0};
unsigned long lastRepeat[buttonCount] = {0};
unsigned long lastEventTime[buttonCount] = {0};
bool isRepeating[buttonCount] = {false};

int lastEnc1A = HIGH;
bool lastEnc1Btn = HIGH;
unsigned long enc1PressTime = 0;
unsigned long enc1LastRepeat = 0;
unsigned long enc1LastEvent = 0;
bool enc1Repeating = false;

int lastEnc2A = HIGH;
bool lastEnc2Btn = HIGH;
unsigned long enc2PressTime = 0;
unsigned long enc2LastRepeat = 0;
unsigned long enc2LastEvent = 0;
bool enc2Repeating = false;

class ServerCallbacks : public NimBLEServerCallbacks {
  void onConnect(NimBLEServer *server, NimBLEConnInfo &connInfo) override {
    (void)server;
    (void)connInfo;
    bleConnected = true;
    Serial.println("[BLE] Client connected");
  }

  void onDisconnect(NimBLEServer *server, NimBLEConnInfo &connInfo, int reason) override {
    (void)server;
    (void)connInfo;
    (void)reason;
    bleConnected = false;
    Serial.println("[BLE] Client disconnected; advertising restarted");
    NimBLEDevice::startAdvertising();
  }
};

void sendEvent(const String &eventText) {
  Serial.println(eventText);

  if (!bleConnected || eventCharacteristic == nullptr) {
    return;
  }

  eventCharacteristic->setValue(eventText.c_str());
  eventCharacteristic->notify();
}

void setupBle() {
  NimBLEDevice::init(DEVICE_NAME);

  NimBLEServer *server = NimBLEDevice::createServer();
  server->setCallbacks(new ServerCallbacks());

  NimBLEService *service = server->createService(SERVICE_UUID);
  eventCharacteristic = service->createCharacteristic(
      EVENT_CHARACTERISTIC_UUID,
      NIMBLE_PROPERTY::READ | NIMBLE_PROPERTY::NOTIFY);
  eventCharacteristic->setValue("START");
  service->start();

  NimBLEAdvertising *advertising = NimBLEDevice::getAdvertising();
  advertising->addServiceUUID(SERVICE_UUID);
  advertising->setName(DEVICE_NAME);
  advertising->enableScanResponse(true);
  advertising->start();

  Serial.println("[BLE] Advertising as KeyBloom-C3");
}

void setup() {
  Serial.begin(115200);

  for (int i = 0; i < buttonCount; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  pinMode(ENC1_A, INPUT_PULLUP);
  pinMode(ENC1_B, INPUT_PULLUP);
  pinMode(ENC1_SW, INPUT_PULLUP);
  pinMode(ENC2_A, INPUT_PULLUP);
  pinMode(ENC2_B, INPUT_PULLUP);
  pinMode(ENC2_SW, INPUT_PULLUP);

  lastEnc1A = digitalRead(ENC1_A);
  lastEnc2A = digitalRead(ENC2_A);

  setupBle();
  sendEvent("START");
}

void loop() {
  handleButtons();
  handleEncoder1();
  handleEncoder2();
  delay(1);
}

void handleButtons() {
  unsigned long now = millis();

  for (int i = 0; i < buttonCount; i++) {
    bool current = digitalRead(buttonPins[i]);

    if (current == LOW && lastButtonState[i] == HIGH) {
      if (now - lastEventTime[i] > DEBOUNCE_TIME) {
        sendEvent("BUTTON " + String(i + 1) + " PRESSED");
        lastEventTime[i] = now;
        pressTime[i] = now;
        lastRepeat[i] = now;
        isRepeating[i] = false;
      }
    }

    if (current == LOW && lastButtonState[i] == LOW) {
      if (!isRepeating[i] && now - pressTime[i] >= REPEAT_DELAY) {
        isRepeating[i] = true;
        lastRepeat[i] = now;
      }

      if (isRepeating[i] && now - lastRepeat[i] >= REPEAT_RATE) {
        sendEvent("BUTTON " + String(i + 1) + " PRESSED");
        lastRepeat[i] = now;
      }
    }

    if (current == HIGH && lastButtonState[i] == LOW) {
      isRepeating[i] = false;
    }

    lastButtonState[i] = current;
  }
}

void handleEncoder1() {
  unsigned long now = millis();
  int encA = digitalRead(ENC1_A);

  // Trigger on one edge only to avoid sending two events per detent.
  if (encA != lastEnc1A && encA == LOW) {
    sendEvent(digitalRead(ENC1_B) != encA ? "ENC1 LEFT" : "ENC1 RIGHT");
  }
  lastEnc1A = encA;

  bool btn = digitalRead(ENC1_SW);
  if (btn == LOW && lastEnc1Btn == HIGH && now - enc1LastEvent > DEBOUNCE_TIME) {
    sendEvent("ENC1 BUTTON PRESSED");
    enc1LastEvent = now;
    enc1PressTime = now;
    enc1LastRepeat = now;
    enc1Repeating = false;
  }

  if (btn == LOW && lastEnc1Btn == LOW) {
    if (!enc1Repeating && now - enc1PressTime >= REPEAT_DELAY) {
      enc1Repeating = true;
      enc1LastRepeat = now;
    }
    if (enc1Repeating && now - enc1LastRepeat >= REPEAT_RATE) {
      sendEvent("ENC1 BUTTON PRESSED");
      enc1LastRepeat = now;
    }
  }

  if (btn == HIGH && lastEnc1Btn == LOW) {
    enc1Repeating = false;
  }
  lastEnc1Btn = btn;
}

void handleEncoder2() {
  unsigned long now = millis();
  int encA = digitalRead(ENC2_A);

  if (encA != lastEnc2A && encA == LOW) {
    sendEvent(digitalRead(ENC2_B) != encA ? "ENC2 LEFT" : "ENC2 RIGHT");
  }
  lastEnc2A = encA;

  bool btn = digitalRead(ENC2_SW);
  if (btn == LOW && lastEnc2Btn == HIGH && now - enc2LastEvent > DEBOUNCE_TIME) {
    sendEvent("ENC2 BUTTON PRESSED");
    enc2LastEvent = now;
    enc2PressTime = now;
    enc2LastRepeat = now;
    enc2Repeating = false;
  }

  if (btn == LOW && lastEnc2Btn == LOW) {
    if (!enc2Repeating && now - enc2PressTime >= REPEAT_DELAY) {
      enc2Repeating = true;
      enc2LastRepeat = now;
    }
    if (enc2Repeating && now - enc2LastRepeat >= REPEAT_RATE) {
      sendEvent("ENC2 BUTTON PRESSED");
      enc2LastRepeat = now;
    }
  }

  if (btn == HIGH && lastEnc2Btn == LOW) {
    enc2Repeating = false;
  }
  lastEnc2Btn = btn;
}
