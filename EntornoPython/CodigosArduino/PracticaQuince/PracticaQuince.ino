#include <WiFi.h>

bool activacion_canal = false;
//const char* ssid = "Mega-2.4G-57AE";
//const char* password = "RT2tXTARhB";

//const char* ssid = "informatica7";
//const char* password = "Info_@@7";

const char* ssid = "Sora";
const char* password = "1234567890";

WiFiServer server(8888);
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
  Serial.println("Cliente conectado");
  Serial.println(WiFi.localIP());

  //Preparamos el servidor
  server.begin();
}

void loop() {

  int valor = random(0,255);
  if(!cliente || !cliente.connected()){
    cliente = server.available();
  }

  cliente.println(valor);
  delay(1000);
  
}
