//PARA LA PRESENTE PRACTICA SE REQUIERE TENER INSTALADA LA LIBRERIA ARDUINO JSON by Benoit
#include <ArduinoJson.h>

void setup() {
  
  Serial.begin(115200);
}

void loop() {
  StaticJsonDocument<200> doc; //El 200 indica la cantidad de valores de atributo a guardar, en este ejemplo es limitado a 200 atributos/
  //StaticJsonDocument.createNestedArray("valor atributo")
  //crea una matriz y la añade a la matriz raíz. 
  //Si la raíz del documento no es una matriz, esta función no realiza ninguna acción. 
  //Si el documento está vacío, esta función inicializa la raíz del documento como una matriz.
  /*{
    "ports": [
        80,
        443
      ]
    }
  */
  JsonArray labels = doc.createNestedArray("labels"); 
  labels.add("A");
  labels.add("B");
  labels.add("C");

  JsonArray values = doc.createNestedArray("values");
  values.add(random(20,100));
  values.add(random(20,100));
  values.add(random(20,100));

  serializeJson(doc,Serial);
  Serial.println();

  delay(1000);
}
