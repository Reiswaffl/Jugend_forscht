
////////////////////////////////// variables 
int button = 2;
////////////////////////////////



void setup() 
{
  Serial.begin(115200);
  pinMode(2,INPUT_PULLUP);
  delay (1000);
    
}

void loop()
{
   if(digitalRead(2) == LOW)// Button pressed
   {
      Serial.println("Hello!");
   }
}
