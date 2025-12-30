// ================= CONFIG =================
const int buttonPins[4] = {3, 21, 5, 6};

// Rotary Encoder pins
#define ENC_A 10
#define ENC_B 20
#define ENC_SW 0

// Timing (ms)
#define DEBOUNCE_TIME 50
#define REPEAT_DELAY  400
#define REPEAT_RATE   80

// ================= STATE =================
int lastEncA = HIGH;

// Button states
bool lastButtonState[4] = {HIGH, HIGH, HIGH, HIGH};
unsigned long pressTime[4] = {0, 0, 0, 0};
unsigned long lastRepeat[4] = {0, 0, 0, 0};
unsigned long lastEventTime[4] = {0, 0, 0, 0};
bool isRepeating[4] = {false, false, false, false};

// Encoder button states
bool lastEncBtn = HIGH;
unsigned long encPressTime = 0;
unsigned long encLastRepeat = 0;
unsigned long encLastEvent = 0;
bool encRepeating = false;

// ================= SETUP =================
void setup() {
  Serial.begin(115200);

  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  pinMode(ENC_A, INPUT_PULLUP);
  pinMode(ENC_B, INPUT_PULLUP);
  pinMode(ENC_SW, INPUT_PULLUP);

  Serial.println("START");
}

// ================= LOOP =================
void loop() {
  handleButtons();
  handleEncoder();
}

// ================= BUTTON HANDLER =================
void handleButtons() {
  unsigned long now = millis();

  for (int i = 0; i < 4; i++) {
    bool current = digitalRead(buttonPins[i]);

    // ----- FIRST PRESS (EDGE + DEBOUNCE) -----
    if (current == LOW && lastButtonState[i] == HIGH) {
      if (now - lastEventTime[i] > DEBOUNCE_TIME) {
        Serial.print("BUTTON ");
        Serial.print(i + 1);
        Serial.println(" PRESSED");

        lastEventTime[i] = now;
        pressTime[i] = now;
        lastRepeat[i] = now;
        isRepeating[i] = false;
      }
    }

    // ----- HOLD → AUTO REPEAT -----
    if (current == LOW && lastButtonState[i] == LOW) {
      if (!isRepeating[i] && (now - pressTime[i] >= REPEAT_DELAY)) {
        isRepeating[i] = true;
        lastRepeat[i] = now;
      }

      if (isRepeating[i] && (now - lastRepeat[i] >= REPEAT_RATE)) {
        Serial.print("BUTTON ");
        Serial.print(i + 1);
        Serial.println(" PRESSED");
        lastRepeat[i] = now;
      }
    }

    // ----- RELEASE -----
    if (current == HIGH && lastButtonState[i] == LOW) {
      isRepeating[i] = false;
    }

    lastButtonState[i] = current;
  }
}

// ================= ENCODER HANDLER =================
void handleEncoder() {
  unsigned long now = millis();

  // ----- ROTATION -----
  int encA = digitalRead(ENC_A);
  if (encA != lastEncA) {
    if (digitalRead(ENC_B) != encA) {
      Serial.println("ENCODER RIGHT");
    } else {
      Serial.println("ENCODER LEFT");
    }
  }
  lastEncA = encA;

  // ----- ENCODER BUTTON -----
  bool encBtn = digitalRead(ENC_SW);

  // FIRST PRESS
  if (encBtn == LOW && lastEncBtn == HIGH) {
    if (now - encLastEvent > DEBOUNCE_TIME) {
      Serial.println("ENCODER BUTTON PRESSED");

      encLastEvent = now;
      encPressTime = now;
      encLastRepeat = now;
      encRepeating = false;
    }
  }

  // HOLD → REPEAT
  if (encBtn == LOW && lastEncBtn == LOW) {
    if (!encRepeating && (now - encPressTime >= REPEAT_DELAY)) {
      encRepeating = true;
      encLastRepeat = now;
    }

    if (encRepeating && (now - encLastRepeat >= REPEAT_RATE)) {
      Serial.println("ENCODER BUTTON PRESSED");
      encLastRepeat = now;
    }
  }

  // RELEASE
  if (encBtn == HIGH && lastEncBtn == LOW) {
    encRepeating = false;
  }

  lastEncBtn = encBtn;
} 