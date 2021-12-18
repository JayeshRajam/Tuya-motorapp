const int ledPin = 32; // the pin that the LED is attached to
String incomingByte;      // a variable to read incoming serial data into
// setting PWM properties
const int freq = 5000;
const int ledChannel = 0;
const int resolution = 8;
 

void setup() {
  // initialize serial communication:
  Serial.begin(115200);
  // configure LED PWM functionalitites
  ledcSetup(ledChannel, freq, resolution);
  
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(ledPin, ledChannel);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    if (incomingByte == "L") {
      ledcWrite(ledChannel,0);
    }
    else {
      ledcWrite(ledChannel,incomingByte.toInt());
    }
    Serial.println(incomingByte);
    delay(100);
    }
  }
