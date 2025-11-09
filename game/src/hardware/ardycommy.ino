#include <LiquidCrystal.h>


LiquidCrystal lcd(12,11,7,6,5,4);
int x;
unsigned long delay_ = 500UL;
int flexs1 = A0;
int flexs2 = A1;
int flexs3 = A2;
int flexs4 = A3;


int flexdata1 = 0;
int flexdata2 = 0;
int flexdata3 = 0;
int flexdata4 = 0;
int output;
char comma[2] = ",";

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  // put your main code here, to run repeatedly:
  flexdata1 = analogRead(flexs1);
  flexdata2 = analogRead(flexs2);
  flexdata3 = analogRead(flexs3);
  flexdata4 = analogRead(flexs4);

  output = (flexdata1 * 10000000) + (flexdata2 * 10000) + (flexdata3 * 1000) + (flexdata4 * 10);

  // formatted printing for 4 sensors
  lcd.setCursor(0, 1);
  lcd.print("    "); // padding
  lcd.setCursor(0, 1);
  lcd.print(flexdata1);

  lcd.setCursor(4, 1);
  lcd.print("    "); // padding
  lcd.setCursor(4, 1);
  lcd.print(flexdata2);

  lcd.setCursor(8, 1);
  lcd.print("    "); // padding
  lcd.setCursor(8, 1);
  lcd.print(flexdata3);

  lcd.setCursor(12, 1);
  lcd.print("    "); // padding
  lcd.setCursor(12, 1);
  lcd.print(flexdata4);

  delay(delay_);

  x = Serial.write(output);
  // while (!Serial.available());
  //   x = Serial.readString().toInt();
  //   lcd.print(x);
}
