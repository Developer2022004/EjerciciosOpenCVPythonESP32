#include <WiFi.h>
#include <ArduinoJson.h>

bool activacion_canal = false;
const char* ssid = "Mega-2.4G-57AE";
const char* password = "RT2tXTARhB";

//const char* ssid = "informatica7";
//const char* password = "Info_@@7";

//Creamos una constante para la IP del servidor
const char* IP = "192.168.100.14";
const int PUERTO_SERVIDOR = 5000;

//const char* ssid = "Sora";
//const char* password = "1234567890";

//WiFiServer server(8888);
WiFiClient cliente;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  //Configuramos WiFi
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectandose....");
  }
  if(cliente.connect(IP,PUERTO_SERVIDOR)){
    Serial.println("Si se conecto al servidor");
  }else{
    Serial.println("No se conecto al servidor");
  }
}

void loop() {

  int valor = random(0,255);

  StaticJsonDocument<100> documento;
  JsonArray claves = documento.createNestedArray("Claves");
  claves.add("Valor");
  JsonArray valores = documento.createNestedArray("Valores");
  claves.add("Valores");
  valores.add(valor);

  String datos;
  //serializeJson(documentoJson,Variable_donde_Se_guardara_en_String)
  serializeJson(documento,datos);

  if(cliente.connected()){
    cliente.println(datos);
  }else{
    if(cliente.connect(IP,PUERTO_SERVIDOR)){
      Serial.println("El cliente se desconecto....");
    }
  }
  delay(1000);
  
}
