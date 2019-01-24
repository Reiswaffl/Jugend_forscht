
////////////////////////////////// variables 
int black = 2;
int yellow = 3;
int white = 4;
int red = 5;
int blue = 6;
////////////////////////////////



void setup() 
{
  Serial.begin(115200);
  pinMode(black,INPUT_PULLUP);
  pinMode(yellow,INPUT_PULLUP);
  pinMode(white,INPUT_PULLUP);
  pinMode(red,INPUT_PULLUP);
  pinMode(blue,INPUT_PULLUP);
  delay (1000);
    
}

void loop()
{
   if(digitalRead(black) == LOW)// Button pressed
   {
      Serial.println("100,100");
      delay(90);
   }
   if(digitalRead(yellow) == LOW){
      Serial.println("-100,-100");
      delay(90);
   }
   if(digitalRead(white) == LOW){
      Serial.println("!0");
      delay(90);
   }
   if(digitalRead(red) == LOW){
      Serial.println("!1");
      delay(90);
   }
   if(digitalRead(blue) == LOW){
      Serial.println("!2");
      delay(90);
   }
}
