https://www.tinkercad.com/things/ecEn0D1D3D3

#include <Servo.h>
#define PIN_LED     13
Servo servo1;
int moisture = 0;
int minval = 200;
int maxval = 600;
int mid = 386;
int pinServo = 12;
void setup()
{
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
  pinMode(12, OUTPUT);
  pinMode(8, OUTPUT);
  servo1.attach(pinServo);
}

void loop()
{
  digitalWrite(A0, HIGH);
  delay(10); // Wait for 10 millisecond(s)
  moisture = analogRead(A1);
  Serial.println(moisture);
  digitalWrite(13, LOW); 
  servo1.write(0);
  digitalWrite(8, LOW); 
  if(moisture < minval){
    if(moisture<mid){
      servo1.write(90);
      digitalWrite(13, HIGH);
    } 
  }else{
    if (moisture > maxval){
      if(moisture>mid){
      digitalWrite(8, HIGH);
    }
       
      
    }
  }
  
}
