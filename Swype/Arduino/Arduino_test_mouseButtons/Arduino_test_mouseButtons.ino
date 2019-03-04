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
      Serial.println("!0");
      delay(40);

   }
   if(digitalRead(yellow) == LOW){
      Serial.println("!1");
      delay(40);

   }
   if(digitalRead(white) == LOW){
      Serial.println("c1");
      delay(40);
      Serial.println("c1");
      delay(40);
   }
   if(digitalRead(red) == LOW){
      Serial.println("s+");
      delay(150);
   }
   if(digitalRead(blue) == LOW){
      Serial.println("s-");
      delay(150);
   }
}
