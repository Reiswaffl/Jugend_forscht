
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
    Serial.println("100,100");
        delay(200);
    Serial.println("20,0");
        delay(200);
    Serial.println("-50,0");
        delay(200);
    Serial.println("-50,-50");
    delay(200);
   }
}
