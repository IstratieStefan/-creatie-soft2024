uint8_t buf[8] = {0};
int buttonpin1 = 5;
int buttonpin2 = 4;
int buzzer = 6;

int buttonState1 = 0;
int buttonState2 = 0;

void setup() {
  pinMode(buttonpin1, INPUT);
  pinMode(buttonpin2, INPUT);
  pinMode(buzzer, OUTPUT);
  //Keyboard.begin();
  Serial.begin(9600);
}

void keyRelease() {
    buf[0] = 0;
    buf[2] = 0;
}

void loop() {
  buttonState1 = digitalRead(buttonpin1);
  buttonState2 = digitalRead(buttonpin2);

  if (buttonState1 == HIGH && buttonState2 == HIGH) {
    //Keyboard.write('/');
    tone(buzzer, 1000); 
    delay(100);
    noTone(buzzer);
    buf[2] = 56; 
    Serial.write(buf, 8);
    keyRelease();
  }
  if (buttonState1 == HIGH && buttonState2 == LOW) {
    //Keyboard.write('-');
    tone(buzzer, 1000); 
    delay(400);
    noTone(buzzer); 
    buf[2] = 45; 
    Serial.write(buf, 8);
    keyRelease();
  }
  if (buttonState1 == LOW && buttonState2 == HIGH) {
    //Keyboard.write('.');
    tone(buzzer, 1000); 
    delay(100);
    noTone(buzzer); 
    buf[2] = 55; 
    Serial.write(buf, 8);
    keyRelease();
  }

}
