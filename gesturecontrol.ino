#include <cvzone.h>

#define BAUDRATE 9600
#define LED1_PIN  13

/* Global variables */
SerialData serialData(1, 3); //(num of vals, digits of val)
int valsRec[1]; //Serial Data Value

/*Setting up the led 
  Params: led_no = pin that led is connected to */
void setup_led(uint8_t led_no)
{
  pinMode(led_no, OUTPUT);
}

/* Set the brightness for LED
  Params: led_no = pin that led is connected to
          brightness = percentage of brightness for the selected led */
void set_brightness(uint8_t led_no, int brightness)
{
  analogWrite(led_no, brightness);
}

/* Set Up code - This code will run once */
void setup() {
  // put your setup code here, to run once:
  serialData.begin(BAUDRATE);
  Serial.begin(BAUDRATE);
  setup_led(LED1_PIN);
}

void loop() {
  // put your main code here, to run repeatedly:
  serialData.Get(valsRec);
  uint8_t brightness = valsRec[0];
  set_brightness(LED1_PIN, brightness);
  Serial.println(brightness);

}
