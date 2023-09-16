//https://www.tinkercad.com/things/aUGLzxB04rb
#include <Servo.h>
#define PIN_LED_HOT     13
#define PIN_LED_COLD     12
#define PIN_POT     A0
Servo servo1;
Servo servo2;
const int pinServo=8; // Пин для подключения сервопривода1
const int pinServo1=10;// Пин для подключения сервопривода2
const int POT=A0; //потенциометр, отвечающий за телоту воды
const int POT1=A1;//потенциометр, отвечающий за напор воды
int valpot = 0; // переменная для хранения значения потенциометра, отвечающего за телоту воды
int valpot1 = 0;// переменная для хранения значения потенциометра, отвечающего за напор воды
int valpot2 = 0;
int angleServo = 0; //переменная для хранения угла поворота

void setup()
{
pinMode(PIN_LED_HOT, OUTPUT);
pinMode(PIN_LED_COLD, OUTPUT);
pinMode(PIN_POT, INPUT);
servo1.attach(pinServo);
servo2.attach(pinServo1);
}
void loop()
{
//Работа со светодиодами
int col, brightness; 
// Считывание в переменную напряжение с резистора и преобразум число в градусы
col = analogRead(PIN_POT);
brightness = map(col,0,1023,0,255);
analogWrite(PIN_LED_HOT, brightness);
analogWrite(PIN_LED_COLD, 255-brightness);
  
//Работа с микросервоприводами
valpot = analogRead(POT); 
valpot2 = analogRead(POT1);
valpot1 = map(valpot2,0,1023,0,180);
angleServo=map(valpot,0,1023,0,valpot1);
// поворот микросервопривода на полученный угол
servo1.write(angleServo);
delay(10);
servo2.write(valpot1-angleServo);
delay(10);
}
