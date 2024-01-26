#include <Keyboard.h>
int buttonpin1 = 5;
int buttonpin2 = 4;
int buzzer = 6;

int buttonState1 = 0;
int buttonState2 = 0;

void setup() {
  pinMode(buttonpin1, INPUT_PULLUP);
  pinMode(buttonpin2, INPUT_PULLUP);
  pinMode(buzzer, OUTPUT);
  //Keyboard.begin();
}

void loop() {
  buttonState1 = digitalRead(buttonpin1);
  buttonState2 = digitalRead(buttonpin2);

  if (buttonState1 == HIGH && buttonState2 == HIGH) {
    //Keyboard.write('/');
    tone(buzzer, 1000); 
    delay(1000);
    noTone(buzzer); 
  }
  if (buttonState1 == HIGH && buttonState2 == LOW) {
    //Keyboard.write('-');
    tone(buzzer, 1000); 
    delay(1000);
    noTone(buzzer); 
  }
  if (buttonState1 == LOW && buttonState2 == HIGH) {
    //Keyboard.write('.');
    tone(buzzer, 1000); 
    delay(1000);
    noTone(buzzer); 
  }

}
