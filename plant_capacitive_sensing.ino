#include <CapacitiveSensor.h>

#define LED_PIN         13       // Pin where the external LED is connected
#define CAP_SEND_PIN    4        // Capacitive send pin
#define CAP_RECEIVE_PIN 2        // Capacitive receive pin

// Create a capacitive sensor instance
CapacitiveSensor capSensor = CapacitiveSensor(CAP_SEND_PIN, CAP_RECEIVE_PIN);    

void setup()                    
{
   pinMode(LED_PIN, OUTPUT);      // Set LED pin as output
   capSensor.set_CS_AutocaL_Millis(0xFFFFFFFF);     // Turn off automatic calibration 
   Serial.begin(9600);             // Start serial communication at 9600 baud
}

void loop()                    
{
    long touchValue = capSensor.capacitiveSensor(30);  // Get capacitive touch value
    
    Serial.println(touchValue);    // Print touch value to Serial Monitor
    
    if (touchValue > 1000)  // Threshold for touch detection, you may need to adjust this
    {
        digitalWrite(LED_PIN, HIGH);   // Turn on the external LED if plant is touched
    }
    else
    {
        digitalWrite(LED_PIN, LOW);    // Turn off the external LED if plant is not touched
    }
}
