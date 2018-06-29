#define BLUE_PIN 3
#define RED_PIN 5
#define GREEN_PIN 6

String input = "";
void setup()
{
    pinMode(RED_PIN, OUTPUT);
    pinMode(GREEN_PIN, OUTPUT);
    pinMode(BLUE_PIN, OUTPUT);

    analogWrite(RED_PIN, 0);
    analogWrite(GREEN_PIN, 0);
    analogWrite(BLUE_PIN, 0);

    Serial.begin(9600);
}
void loop()
{
    while (Serial.available())
    {
        if (Serial.available() > 0)
        {
            char serialData = Serial.read();
            input += serialData;
        }
    }
    if (input.length() > 8)
    {
        analogWrite(RED_PIN, input.substring(0, 3).toInt());
        analogWrite(GREEN_PIN, input.substring(3, 6).toInt());
        analogWrite(BLUE_PIN, input.substring(6).toInt());
        input = "";
    }
    delay(10);
}