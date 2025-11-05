//PARA LA PRESENTE PRACTICA SE REQUIERE TENER INSTALADA LA LIBRERIA ARDUINO JSON by Benoit
#include <ArduinoJson.h>

void setup() {
//  pinMode(potenciometro,INPUT);
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<100> doc; //El 200 indica la cantidad de valores de atributo a guardar, en este ejemplo es limitado a 200 atributos/
  doc["Labels"] = "Sensor";
  doc["values"] = random(10,200);

  serializeJson(doc,Serial);//Enviamos el json a traves del Serial.
  Serial.println();

  delay(1000);
}
