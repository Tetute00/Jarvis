/*
 * ESP32 Color Sensor - Proyecto Jarvis
 * 
 * Este c�digo maneja un sensor de color conectado al ESP32 y comunica
 * los resultados al servidor principal mediante WiFi.
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>

// Definiciones para el sensor de color (ajustar seg�n el modelo espec�fico)
#define COLOR_SENSOR_ADDR 0x29

// Configuraci�n WiFi
const char* ssid = "JarvisNetwork";
const char* password = "your_secure_password";
const char* serverUrl = "http://your_server_ip:8000/color";

void setup() {
  Serial.begin(115200);
  
  // Iniciar conexi�n WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi conectado!");
  
  // Inicializar el sensor de color
  Wire.begin();
  initColorSensor();
}

void loop() {
  // Leer datos del sensor de color
  int red, green, blue;
  readColorValues(&red, &green, &blue);
  
  // Enviar datos al servidor
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    
    String colorJson = "{"red":" + String(red) + 
                       ","green":" + String(green) + 
                       ","blue":" + String(blue) + "}";
                       
    int httpResponseCode = http.POST(colorJson);
    
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println("Respuesta del servidor: " + response);
    } else {
      Serial.print("Error en la petici�n HTTP: ");
      Serial.println(httpResponseCode);
    }
    
    http.end();
  }
  
  delay(2000); // Esperar 2 segundos entre lecturas
}

void initColorSensor() {
  // C�digo de inicializaci�n espec�fico para tu sensor de color
  // Este es un lugar reservado, necesitar�s ajustarlo seg�n el sensor exacto
  Serial.println("Sensor de color inicializado");
}

void readColorValues(int* red, int* green, int* blue) {
  // C�digo para leer los valores RGB del sensor
  // Este es un lugar reservado, necesitar�s ajustarlo seg�n el sensor exacto
  
  // Simulaci�n de lecturas para pruebas
  *red = random(0, 255);
  *green = random(0, 255);
  *blue = random(0, 255);
  
  Serial.print("RGB: (");
  Serial.print(*red);
  Serial.print(", ");
  Serial.print(*green);
  Serial.print(", ");
  Serial.print(*blue);
  Serial.println(")");
}
