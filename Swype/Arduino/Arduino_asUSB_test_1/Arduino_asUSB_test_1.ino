
////////////////////////////////// variables 
int button = 2;
////////////////////////////////



void setup() 
{
  Serial.begin(9600);
  pinMode(2,INPUT_PULLUP);
  delay (1000);
    
}

void loop()
{
   if(digitalRead(2) == LOW)// Button pressed
   {
    Serial.println("up");
    delay(90);
   }
}
