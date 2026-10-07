// Morse receiver: listens on Serial for '.' and '-' and blinks an LED.
// Wiring: Pin 8 -> LED anode (+); LED cathode (-) -> 220 ohm resistor -> GND

const int LED_PIN = 8;          // external LED (use 13 for the on-board LED)
const int DOT_MS = 200;         // dot duration
const int DASH_MS = 600;        // dash = 3x dot (Morse timing rule)
const int GAP_MS = 200;         // gap between symbols

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);           // must match baud rate in Python
  delay(100);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == '.') {
      blinkLed(DOT_MS);
    } else if (c == '-') {
      blinkLed(DASH_MS);
    }
    // any other character is ignored
  }
}

void blinkLed(int onTime) {
  digitalWrite(LED_PIN, HIGH);
  delay(onTime);
  digitalWrite(LED_PIN, LOW);
  delay(GAP_MS);
}
