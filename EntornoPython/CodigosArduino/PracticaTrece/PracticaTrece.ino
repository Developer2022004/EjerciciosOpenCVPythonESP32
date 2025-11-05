#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth no esta habilitado
#endif

BluetoothSerial puerto;


void setup() {
  // put your setup code here, to run once:
  puerto.begin("ESP32Mane");
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int valor = random(1,100);
  puerto.println(valor);
  delay(1000);
}
