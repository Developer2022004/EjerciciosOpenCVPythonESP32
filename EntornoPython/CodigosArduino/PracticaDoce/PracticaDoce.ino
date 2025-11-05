#include <ArduinoJson.h>

bool encendido = true;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  StaticJsonDocument<100> documento;
  if(encendido){
    int valor = random(1,100);
    int valor_dos = random(1,100);

    JsonArray atributos = documento.createNestedArray("atributos");
    JsonArray valores = documento.createNestedArray("valores");
    atributos.add("valor");
    atributos.add("valor_dos");
    valores.add(valor);
    valores.add(valor_dos);

    serializeJson(documento,Serial);
    Serial.println();
  }

  //Preguntamos para recibir el valor de arranque desde la interfaz del microcontrolador
  if(Serial.available()){
    char c = Serial.read();
    if(c == '1'){
      encendido = !encendido;
    }
  }
  delay(1000);
}
