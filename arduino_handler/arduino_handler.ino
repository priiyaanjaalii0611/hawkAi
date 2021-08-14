#include <Servo.h>
#include <EEPROM.h>

Servo servo1;
Servo servo2;
int flag = 0;
int flagMem = 8;
int mem1 = 0;
int mem2 = 4;

void setup() {
  servo1.attach(9);
  servo2.attach(7);
  Serial.begin(9600);
  servo1.write(EEPROM.read(mem1));
  servo2.write(EEPROM.read(mem2));
  flag= EEPROM.read(flagMem);
}

void loop() {
  if(Serial.available()){
    if(flag){
      EEPROM.update(mem1,Serial.readString().toInt());
//      Serial.println(pos1);
//      Serial.flush();
      EEPROM.write(flagMem, (flag+1)%2);
    }
    if(!flag)
      EEPROM.update(mem2,Serial.readString().toInt());
      EEPROM.write(flagMem, (flag+1)%2);
//      Serial.println(pos2);
//      Serial.flush();
  }
  servo1.write(EEPROM.read(mem1));
  servo2.write(EEPROM.read(mem2));
}
