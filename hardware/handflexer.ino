#include <LiquidCrystal.h>


LiquidCrystal lcd(12,11,7,6,5,4);
int x;
unsigned long delay_ = 400UL;
int flexs1 = A0;
int flexs2 = A1;
int flexs3 = A2;
int flexs4 = A3;

int flexdata1 = 0;
int flexdata2 = 0;
int flexdata3 = 0;
int flexdata4 = 0;
int output = 0;

int init1;
int init2;
int init3;
int init4;

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  Serial.begin(115200);
  Serial.setTimeout(1);

  init1 = analogRead(flexs1);
  init2 = analogRead(flexs2);
  init3 = analogRead(flexs3);
  init4 = analogRead(flexs4);

}

void loop() {
  output = 2222;
  // put your main code here, to run repeatedly:
  flexdata1 = analogRead(flexs1);
  flexdata2 = analogRead(flexs2);
  flexdata3 = analogRead(flexs3);
  flexdata4 = analogRead(flexs4);

  if (flexdata1 < (init1-5)){
    output = output - 1000;
  }
  if (flexdata2 <= (init2-4)){
    output = output - 100;
  }
  if (flexdata3 <= (init3-5)){
    output = output - 10;
  }
  if (flexdata4 <= (init4-5)){
    output = output - 1;
  }

  // formatted printing for 4 sensors
  lcd.setCursor(0, 0);
  lcd.print("Out: "); lcd.print(output);
  lcd.setCursor(0, 1);
  lcd.print(flexdata1); lcd.print(' ');
  lcd.print(flexdata2); lcd.print(' ');
  lcd.print(flexdata3); lcd.print(' ');
  lcd.print(flexdata4);
  
  delay(delay_);

  if (Serial){
      Serial.println(output);
  }
  // while (!Serial.available());
  //   x = Serial.readString().toInt();
  //   lcd.print(x);
}
