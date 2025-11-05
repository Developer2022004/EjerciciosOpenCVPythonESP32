#include <ArduinoJson.h>
#define tdsSensorPin 34   
#define VREF 3.3          
#define ADC_RANGE 4095.0  
#define TDS_FACTOR 500   
#define temp_pin 4 
#define foto_celda 32

#include <OneWire.h>
#include <DallasTemperature.h>


OneWire ourWire1(temp_pin);
DallasTemperature sensors1(&ourWire1);   

void setup() {
  
  Serial.begin(115200);

  pinMode(tdsSensorPin, INPUT);
  pinMode(foto_celda,INPUT);

  sensors1.begin();
}

void loop() {
  // --- Lectura de temperatura ---
  sensors1.requestTemperatures();         // Pedir temperatura al sensor
  float temp = sensors1.getTempCByIndex(0); // Obtener temperatura en grados Celsius

  // --- Lectura del sensor TDS ---
  int analogValue = analogRead(tdsSensorPin);  // Leer señal analógica
  float voltage = analogValue * (VREF / ADC_RANGE); // Convertir a voltaje

  // --- Lectura de la fotocelda
  int foto_celda_valor = analogRead(foto_celda);
  foto_celda_valor = map(foto_celda_valor,0,4095,1,400);

  // Compensación de temperatura
  float compensationCoefficient = 1.0 + 0.02 * (temp - 25.0); // Ajuste por temperatura
  float compensatedVoltage = voltage / compensationCoefficient; // Voltaje corregido
  float tdsValue = compensatedVoltage * TDS_FACTOR; // Conversión a ppm

  // Conductividad eléctrica
  float factor_conversion = 0.5;  //Calibrar acorde al tipo de agua
  float EC = tdsValue / factor_conversion;

  //EC - CONDUCTIVIDAD uS/cm
  //tdsValue - TDS PPM
  //foto_celda_valor  - valor foto celda
  //temp - Temperatura °C

  //Crear Documento con Arduino JSON
  StaticJsonDocument<200> doc; 
  JsonArray labels = doc.createNestedArray("labels"); 
  labels.add("A");
  doc["labels"] = "SENSOR";
  doc["temp"] = (int) temp;
  doc["conductividad"] = (int) EC;
  doc["tds"] = (int) tdsValue;
  doc["foto_celda"] = foto_celda_valor;

  serializeJson(doc,Serial);
  Serial.println();
  delay(2000); // Esperar 5 segundos antes de la siguiente lectura
}


