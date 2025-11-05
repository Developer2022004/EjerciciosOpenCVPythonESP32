//PARA LA PRESENTE PRACTICA SE REQUIERE TENER INSTALADA LA LIBRERIA ARDUINO JSON by Benoit
//Nota: el presente sketch funciona tanto para la practica ocho, como la nueve y diez, seis y siete
#include <ArduinoJson.h>
#define potenciometro 32

void setup() {
  pinMode(potenciometro,INPUT);
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<100> doc; //El 200 indica la cantidad de valores de atributo a guardar, en este ejemplo es limitado a 200 atributos/
  int valores = analogRead(potenciometro);
  valores = map(valores,1,4096,1,200);
  doc["labels"] = "Sensor";
  doc["values"] = valores;

  serializeJson(doc,Serial);//Enviamos el json a traves del Serial.
  Serial.println();

  delay(1000);
}
