// https://wokwi.com/projects/318864638990090834

// This version uses bit-banged SPI.
// If you see tearing (jagged edges on the circles) try the version
// which uses AVR's hardware SPI peripheral:
// https://wokwi.com/arduino/projects/318868939929027156

#define CLK 13
#define DIN 11
#define CS  10
#define X_SEGMENTS   4
#define Y_SEGMENTS   4
#define NUM_SEGMENTS (X_SEGMENTS * Y_SEGMENTS)

// a framebuffer to hold the state of the entire matrix of LEDs
// laid out in raster order, with (0, 0) at the top-left
byte fb[8 * NUM_SEGMENTS];
int x_1[35] = {12,13,14,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15,16,15};
int y_1[35] = {11,10,9,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24};

int x_2[72] = {11,12,13,14,15,16,17,18,19,11,12,13,14,15,16,17,18,19,18,19,18,19,18,19,18,19,18,19,18,19,17,16,15,14,13,12,11,17,16,15,14,13,12,11,11,12,11,12,11,12,11,12,11,12,11,12,11,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19};
int y_2[72] = {9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,11,11,12,12,13,13,14,14,15,15,16,16,16,15,16,15,16,15,16,15,16,15,16,15,16,15,17,18,19,20,21,22,23,17,18,19,20,21,22,23,22,23,22,23,22,23,22,23,22,23,22,23,22,23};

int x_3[76] = {11,12,13,14,15,16,17,18,19,11,12,13,14,15,16,17,18,19,18,19,18,19,18,19,18,19,18,19,18,19,17,16,15,14,13,12,11,17,16,15,14,13,12,11,18,19,18,19,18,19,18,19,18,19,18,19,18,19,13,13,14,14,15,15,16,16,17,17,18,18,19,19,12,11,12,11};
int y_3[76] = {9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,11,11,12,12,13,13,14,14,15,15,16,16,16,15,16,15,16,15,16,15,16,15,16,15,16,15,17,18,19,20,21,22,23,17,18,19,20,21,22,23,22,23,22,23,22,23,22,23,22,23,22,23,22,23,22,22,23,23};

int x_4[58] = {11,12,11,12,11,12,11,12,11,12,11,12,11,12,11,12,11,12,13,14,15,16,17,13,14,15,16,17,19,19,19,19,19,19,19,19,19,19,19,19,19,19,18,18,18,18,18,18,18,18,18,18,18,18,18,18};
int y_4[58] = {9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,16,16,16,16,16,17,17,17,17,17,9,10,11,12,13,14,15,16,17,18,19,20,21,22,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23};
int user_names[3] = {'1','2','4'};
int dt[3] = {3,5,10};
int k = 0;

void shiftAll(byte send_to_address, byte send_this_data)
{
  digitalWrite(CS, LOW);
  for (int i = 0; i < NUM_SEGMENTS; i++) {
    shiftOut(DIN, CLK, MSBFIRST, send_to_address);
    shiftOut(DIN, CLK, MSBFIRST, send_this_data);
  }
  digitalWrite(CS, HIGH);
}


void setup() {
  Serial.begin(115200);
  pinMode(CLK, OUTPUT);
  pinMode(DIN, OUTPUT);
  pinMode(CS, OUTPUT);

  // Setup each MAX7219
  shiftAll(0x0f, 0x00); //display test register - test mode off
  shiftAll(0x0b, 0x07); //scan limit register - display digits 0 thru 7
  shiftAll(0x0c, 0x01); //shutdown register - normal operation
  shiftAll(0x0a, 0x0f); //intensity register - max brightness
  shiftAll(0x09, 0x00); //decode mode register - No decode
}


void loop() {
  //clear();
  k=k+1;
  int ind = time_k(k);
  Serial.println();
  if (ind!=-1){
    if (user_names[ind]=='1'){
      first_user(x_1,y_1);
      
    }
    else if (user_names[ind]=='2'){
      second_user(x_2,y_2);
      //k = k+1;
    }
    else if (user_names[ind]=='3'){
      third_user(x_3,y_3);
      //k = k+1;
    }
    else if (user_names[ind]=='4'){
      forth_user(x_4,y_4);
      //k = k+1;
    }

  }
      //show();

  delay(1000);
  clear();
  show();
}  


int time_k(int k){
  int i;
  int p;
  for(i=0;i<sizeof(dt);i++){
    Serial.println(k);
    Serial.println(i);
    Serial.println();
    if (k==dt[i]){
      return i;
    }
  }
  return -1;
}

void first_user(int x_1[35],int y_1[35]){
  for (int i=0;i<35;i++){
    set_pixel(x_1[i],y_1[i],1);
    show();
  }

    delay(1000);

  clear();
}

void second_user(int x_2[72],int y_2[72]){
   for (int i=0;i<72;i++){
    set_pixel(x_2[i],y_2[i],1);
    show();
  }
  delay(1000);
  clear();
}

void third_user(int x_3[76],int y_3[76]){
   for (int i=0;i<76;i++){
    set_pixel(x_3[i],y_3[i],1);
    show();
  }
  delay(1000);
  clear();
}

void forth_user(int x_4[58],int y_4[58]){
   for (int i=0;i<56;i++){
    set_pixel(x_4[i],y_4[i],1);
    show();
  }
  delay(1000);
  clear();
}

void set_pixel(uint8_t x, uint8_t y, uint8_t mode) {
  byte *addr = &fb[x / 8 + y * X_SEGMENTS];
  byte mask = 128 >> (x % 8);
  switch (mode) {
    case 0: // clear pixel
      *addr &= ~mask;
      break;
    case 1: // plot pixel
      *addr |= mask;
      break;
    case 2: // XOR pixel
      *addr ^= mask;
      break;
  }
}


// void safe_pixel(uint8_t x, uint8_t y, uint8_t mode) {
//   if ((x >= X_SEGMENTS * 8) || (y >= Y_SEGMENTS * 8))
//     return;
//   set_pixel(x, y, mode);
// }


// // turn off every LED in the framebuffer
// void clear() {
//   byte *addr = fb;
//   for (byte i = 0; i < 8 * NUM_SEGMENTS; i++)
//     *addr++ = 0;
// }


// send the raster order framebuffer in the correct order
// for the boustrophedon layout of daisy-chained MAX7219s
void clear() {
  byte *addr = fb;
  for (byte i = 0; i < 8 * NUM_SEGMENTS; i++)
    *addr++ = 0;
}

void show() {
  for (byte row = 0; row < 8; row++) {
    digitalWrite(CS, LOW);
    byte segment = NUM_SEGMENTS;
    while (segment--) {
      byte x = segment % X_SEGMENTS;
      byte y = segment / X_SEGMENTS * 8;
      byte addr = (row + y) * X_SEGMENTS;

      if (segment & X_SEGMENTS) { // odd rows of segments
        shiftOut(DIN, CLK, MSBFIRST, 8 - row);
        shiftOut(DIN, CLK, LSBFIRST, fb[addr + x]);
      } else { // even rows of segments
        shiftOut(DIN, CLK, MSBFIRST, 1 + row);
        shiftOut(DIN, CLK, MSBFIRST, fb[addr - x + X_SEGMENTS - 1]);
      }
    }
    digitalWrite(CS, HIGH);
  }
}