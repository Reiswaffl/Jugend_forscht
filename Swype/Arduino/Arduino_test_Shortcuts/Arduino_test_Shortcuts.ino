
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
      Serial.println("n1");
      delay(90);
   }
   if(digitalRead(yellow) == LOW){
      Serial.println("n+");
      delay(150);
   }
   if(digitalRead(white) == LOW){
      Serial.println("n3");
      delay(150);
   }
   if(digitalRead(red) == LOW){
      Serial.println("n=");
      delay(150);
   }
   if(digitalRead(blue) == LOW){
      Serial.println("n4");
      delay(150);
   }
}
