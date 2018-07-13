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
    if (input.length() == 4)
    {
        if (input[0] == 'r')
            analogWrite(RED_PIN, input.substring(1).toInt());
        
        else if (input[0] == 'g')
            analogWrite(GREEN_PIN, input.substring(1).toInt());

        else if(input[0] == 'b')
            analogWrite(BLUE_PIN, input.substring(1).toInt());

        input = "";
    }
    delay(10);
}