#include <AFMotor.h>
AF_DCMotor M1(1);
AF_DCMotor M2(2);
AF_DCMotor M3(3);
AF_DCMotor M4(4);
bool run = false; 
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read the input string from Serial
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim();

    // Parse the input string
    int motorNumber = input.charAt(0) - '0';
    int speed = (input.charAt(2) - '0') * 100 + (input.charAt(3) - '0') * 10 + (input.charAt(4) - '0');
    int duration = (input.charAt(6) - '0') * 1000 + (input.charAt(7) - '0') * 100 + (input.charAt(8) - '0') * 10 + (input.charAt(9) - '0');
    // DEFINED VARS FORWARD 1 BACKWARD 2 BRAKE 3 RELEASE 4
    // can be 1 or 2 
    int direction = (input.charAt(11) - '0');
    // Run the specified motor at the specified speed for the specified duration
    switch (motorNumber) {
      case 1:
        Serial.println("MOTORNUMBER-" + String(motorNumber) + "-SPEED-" + String(speed) + "-DURATION-" + String(duration)+ "-DIRECTION-" + String(direction));      
        M1.setSpeed(speed);
        M1.run(direction);
        delay(duration);
        M1.run(RELEASE);
        break;
      case 2:
        Serial.println("MOTORNUMBER-" + String(motorNumber) + "-SPEED-" + String(speed) + "-DURATION-" + String(duration)+ "-DIRECTION-" + String(direction));
        M2.setSpeed(speed);
        M2.run(direction);
        delay(duration);
        M2.run(RELEASE);
        break;
      case 3:
        Serial.println("MOTORNUMBER-" + String(motorNumber) + "-SPEED-" + String(speed) + "-DURATION-" + String(duration)+ "-DIRECTION-" + String(direction));
        M3.setSpeed(speed);
        M3.run(direction);
        delay(duration);
        M3.run(RELEASE);
        break;
      case 4:
        Serial.println("MOTORNUMBER-" + String(motorNumber) + "-SPEED-" + String(speed) + "-DURATION-" + String(duration)+ "-DIRECTION-" + String(direction));
        M4.setSpeed(speed);
        M4.run(direction);
        delay(duration);
        M4.run(RELEASE);
        break;        
      default:
        Serial.println("Invalid motor number");
        break;
    }
    run = false;    
    // Print out what the program did
    // Serial.print("Motor ");
    // Serial.print(motorNumber);
    // Serial.print(" ran at speed ");
    // Serial.print(speed);
    // Serial.print(" for ");
    // Serial.print(duration);
    // Serial.println(" milliseconds");
  }
}
