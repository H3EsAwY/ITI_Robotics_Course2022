


// Arduino Pins 

#define TMP    A0
#define LED    2
#define SWITCH 3


int reading;
float voltage;
float temperatureC;

void setup()
{
  Serial.begin(9600);
  
  pinMode(TMP, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(SWITCH, INPUT_PULLUP);
  
}

void loop()
{
  
  reading = analogRead(TMP);
  voltage = reading * 5.0;
  voltage /= 1024.0;
  temperatureC = (voltage - 0.5) * 100;
  Serial.print(temperatureC); Serial.println(" degrees C");


  // when an input pullup switch is pressed, it will have a LOW state.
  if((temperatureC > 40) && (digitalRead(SWITCH) == HIGH))
  {
    digitalWrite(LED, HIGH);
  }
  else if((temperatureC > 40) && (digitalRead(SWITCH) == LOW))
  {
    digitalWrite(LED, LOW);
  }
  else
  {
    digitalWrite(LED, LOW);
  }
  
  delay(250);

}
