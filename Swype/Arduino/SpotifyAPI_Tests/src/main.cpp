#include <Arduino.h>
#define next 3
#define last 4
#define play 4

void setup() {
  // put your setup code here, to run once:
  pinMode(next,INPUT_PULLUP);
  pinMode(last,INPUT_PULLUP);
  pinMode(play,INPUT_PULLUP);
  Serial.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(next) == LOW){ Serial.println("SPnext");}
  if(digitalRead(last) == LOW){Serial.println("SPlast");}
  if(digitalRead(play) == LOW){Serial.println("SPplay");}
  if(Serial.read() != NULL){
    // Code to do, when there is data incoming 
  }
}