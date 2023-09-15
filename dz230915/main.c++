// C++ code
//
#include <Servo.h>

int pos9 = 0;
int pos10 = 0;
Servo servo_9;
Servo servo_10;
int LED_PIN1 = 13;
int LED_PIN2 = 12;

void setup()
{
  pinMode(LED_PIN1, OUTPUT);
  pinMode(LED_PIN2, OUTPUT);
  servo_9.attach(9, 500, 2500);
}

void loop()
{
  pos9 = 90;
  servo_9.write(pos9);
  if (pos == 90){
    digitalWrite(LED_PIN2, HIGH);
    delay(1000);
    digitalWrite(LED_PIN2, LOW);
  }
    
  digitalWrite(LED_PIN1, HIGH);
  //digitalWrite(LED_PIN2, HIGH);
  //delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_PIN1, LOW);
  //digitalWrite(LED_PIN2, LOW);
  //delay(1000); // Wait for 1000 millisecond(s)
  
}
