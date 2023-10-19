#include <CapacitiveSensor.h>

#define LED_PIN 13

// Define pins for capacitive sensor
#define CAP_SEND_PIN 4
#define CAP_RECEIVE_PIN 2

// Create capacitive sensor instance
CapacitiveSensor capSensor = CapacitiveSensor(CAP_SEND_PIN, CAP_RECEIVE_PIN);

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  capSensor.set_CS_AutocaL_Millis(0xFFFFFFFF);
}

void loop() {
  long sensorValue = capSensor.capacitiveSensor(30);
  long threshold = 1000;  // Adjust this value based on your setup

  if (sensorValue > threshold) {
    Serial.println("Touch");
    digitalWrite(LED_PIN, HIGH);
  } else {
    digitalWrite(LED_PIN, LOW);
  }
  delay(100);
}
