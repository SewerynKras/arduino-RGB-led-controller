#define BLUE_PIN 3
#define RED_PIN 5
#define GREEN_PIN 6

byte RED_VALUE = 0;
byte GREEN_VALUE = 0;
byte BLUE_VALUE = 0;

void setup()
{
    pinMode(RED_PIN, OUTPUT);
    pinMode(GREEN_PIN, OUTPUT);
    pinMode(BLUE_PIN, OUTPUT);

    changeColor();

    Serial.begin(9600);
}
void loop()
{
    if (Serial.available() > 0)
    {
        byte color = Serial.read();
        byte value = Serial.read();
        {

            // 0 == red
            // 1 == green
            // 2 == blue
            if (color == 0)
                RED_VALUE = value;
            else if (color == 1)
                GREEN_VALUE = value;
            else if (color == 2)
                BLUE_VALUE = value;
        }
    }
    changeColor();
    delay(20);
}

void changeColor()
{
    analogWrite(RED_PIN, RED_VALUE);
    analogWrite(GREEN_PIN, GREEN_VALUE);
    analogWrite(BLUE_PIN, BLUE_VALUE);
}
