// ================= CONFIG =================
const int buttonPins[6] = {0, 1, 2, 3, 4, 20};
const int buttonCount = sizeof(buttonPins) / sizeof(buttonPins[0]);

// Rotary Encoder 1
#define ENC1_A 6
#define ENC1_B 7
#define ENC1_SW 5

// Rotary Encoder 2
#define ENC2_SW 8
#define ENC2_A  9
#define ENC2_B  10

// Timing (ms)
#define DEBOUNCE_TIME 50
#define REPEAT_DELAY  400
#define REPEAT_RATE   80

// ================= STATE =================

// ---------- BUTTON ----------
bool lastButtonState[buttonCount] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};
unsigned long pressTime[buttonCount] = {0};
unsigned long lastRepeat[buttonCount] = {0};
unsigned long lastEventTime[buttonCount] = {0};
bool isRepeating[buttonCount] = {false};

// ---------- ENCODER 1 ----------
int lastEnc1A = HIGH;
bool lastEnc1Btn = HIGH;
unsigned long enc1PressTime = 0;
unsigned long enc1LastRepeat = 0;
unsigned long enc1LastEvent = 0;
bool enc1Repeating = false;

// ---------- ENCODER 2 ----------
int lastEnc2A = HIGH;
bool lastEnc2Btn = HIGH;
unsigned long enc2PressTime = 0;
unsigned long enc2LastRepeat = 0;
unsigned long enc2LastEvent = 0;
bool enc2Repeating = false;

// ================= SETUP =================
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

  Serial.println("START");
}

// ================= LOOP =================
void loop() {
  handleButtons();
  handleEncoder1();
  handleEncoder2();
}

// ================= BUTTON HANDLER =================
void handleButtons() {
  unsigned long now = millis();

  for (int i = 0; i < buttonCount; i++) {
    bool current = digitalRead(buttonPins[i]);

    // FIRST PRESS
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

    // HOLD → REPEAT
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

    // RELEASE
    if (current == HIGH && lastButtonState[i] == LOW) {
      isRepeating[i] = false;
    }

    lastButtonState[i] = current;
  }
}

// ================= ENCODER 1 =================
void handleEncoder1() {
  unsigned long now = millis();

  // ROTATION
  int encA = digitalRead(ENC1_A);
  if (encA != lastEnc1A) {
    if (digitalRead(ENC1_B) != encA) {
      Serial.println("ENC1 LEFT");
    } else {
      Serial.println("ENC1 RIGHT");
    }
  }
  lastEnc1A = encA;

  // BUTTON
  bool btn = digitalRead(ENC1_SW);

  if (btn == LOW && lastEnc1Btn == HIGH) {
    if (now - enc1LastEvent > DEBOUNCE_TIME) {
      Serial.println("ENC1 BUTTON PRESSED");
      enc1LastEvent = now;
      enc1PressTime = now;
      enc1LastRepeat = now;
      enc1Repeating = false;
    }
  }

  if (btn == LOW && lastEnc1Btn == LOW) {
    if (!enc1Repeating && (now - enc1PressTime >= REPEAT_DELAY)) {
      enc1Repeating = true;
      enc1LastRepeat = now;
    }

    if (enc1Repeating && (now - enc1LastRepeat >= REPEAT_RATE)) {
      Serial.println("ENC1 BUTTON PRESSED");
      enc1LastRepeat = now;
    }
  }

  if (btn == HIGH && lastEnc1Btn == LOW) {
    enc1Repeating = false;
  }

  lastEnc1Btn = btn;
} 

// ================= ENCODER 2 =================
void handleEncoder2() {
  unsigned long now = millis();

  // ROTATION
  int encA = digitalRead(ENC2_A);
  if (encA != lastEnc2A) {
    if (digitalRead(ENC2_B) != encA) {
      Serial.println("ENC2 LEFT");
    } else {
      Serial.println("ENC2 RIGHT");
    }
  }
  lastEnc2A = encA;

  // BUTTON
  bool btn = digitalRead(ENC2_SW);

  if (btn == LOW && lastEnc2Btn == HIGH) {
    if (now - enc2LastEvent > DEBOUNCE_TIME) {
      Serial.println("ENC2 BUTTON PRESSED");
      enc2LastEvent = now;
      enc2PressTime = now;
      enc2LastRepeat = now;
      enc2Repeating = false;
    }
  }

  if (btn == LOW && lastEnc2Btn == LOW) {
    if (!enc2Repeating && (now - enc2PressTime >= REPEAT_DELAY)) {
      enc2Repeating = true;
      enc2LastRepeat = now;
    }

    if (enc2Repeating && (now - enc2LastRepeat >= REPEAT_RATE)) {
      Serial.println("ENC2 BUTTON PRESSED");
      enc2LastRepeat = now;
    }
  }

  if (btn == HIGH && lastEnc2Btn == LOW) {
    enc2Repeating = false;
  }

  lastEnc2Btn = btn;
}
