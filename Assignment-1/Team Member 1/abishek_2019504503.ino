#include <Servo.h>

int output1Value = 0;
int sen1Value = 0;
int sen2Value = 0;
int const LDR = A0;


int USdis(int triggerPin, int echoPin)
{
  	pinMode(triggerPin, OUTPUT);
  	digitalWrite(triggerPin, LOW);
  	delayMicroseconds(2);
  	digitalWrite(triggerPin, HIGH);
  	delayMicroseconds(10);
 	digitalWrite(triggerPin, LOW);
  	pinMode(echoPin, INPUT);
 	return pulseIn(echoPin, HIGH);
}

Servo servo_7;

void setup()
{
	Serial.begin(9600);	
  	pinMode(A0, INPUT);
  	pinMode(13, INPUT);
  	servo_7.attach(7, 500, 2500);
  	pinMode(8,OUTPUT);
}

void loop()
{
    int val1 = analogRead(LDR);
  	if (val1 > 90) 
  	{
    	digitalWrite(8, HIGH);
    	Serial.print("Bulb OFF = ");
    	Serial.print(val1);
  	} 
  	else 
  	{
    	digitalWrite(8, LOW);
    	Serial.print("Bulb ON = ");
    	Serial.print(val1);
  	}

  	sen1Value = 0.01723 * USdis(6, 6);
  	if (sen1Value < 100) 
  	{
    	servo_7.write(90);
    	Serial.print("Door is Open: Distance = ");
    	Serial.print(sen1Value);
    	Serial.print("\n");
      	delay(1000);
    	servo_7.write(0);
    	Serial.print("Door is Closed: Distance =  ");
    	Serial.print(sen1Value);
    	Serial.print("\n");
  	} 
  	else 
  	{
    	servo_7.write(0);
    	Serial.print(" 	  || Door Closed! ; Distance =  ");
    	Serial.print(sen1Value);
    	Serial.print("\n");
  	}
 	delay(10);
  

}