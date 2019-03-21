#define next 3
#define last 4
#define play 5
#define start 2
#define green 10
#define yellow 9
#define red 8

void setup() {
  // put your setup code here, to run once:
  pinMode(next,INPUT_PULLUP);
  pinMode(last,INPUT_PULLUP);
  pinMode(play,INPUT_PULLUP);
  pinMode(start,INPUT_PULLUP);

  pinMode(green,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(red,OUTPUT);

  Serial.begin(115200);
 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(next) == LOW){Serial.println("SPforward");
  delay(500);}
  if(digitalRead(last) == LOW){Serial.println("SPback");
  delay(500);}
  if(digitalRead(play) == LOW){Serial.println("SPplay");
  delay(500);}
  if(digitalRead(start) == LOW){Serial.println("SPstartSpotify");
  delay(500);}
}
