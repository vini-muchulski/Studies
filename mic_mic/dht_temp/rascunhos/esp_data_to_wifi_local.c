#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

const char* ssid = "Starlink"; // "SUA_REDE_WIFI"
const char* password = "diversao"; // "SUA_SENHA"

DHT dht(26,DHT11);

void setup() {

  dht.begin();
  delay(2000);

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando ao WiFi...");
  }
  Serial.println("Conectado ao WiFi");

  Serial.println("Endereço de IP: ");
  Serial.println(WiFi.localIP());

}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin("http://192.168.0.106:8080");  // Substitua pelo IP do seu computador
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");

    float temp = dht.readTemperature();
    float umidade = dht.readHumidity();

    String data = "Este é o dado que quero enviar";

    data = "TEMP C " + String(temp) + " -- Umidade " + String(umidade) + " %" ;
    
    int httpResponseCode = http.POST(data);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Erro no envio, código: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  }
  delay(5000); // Envia a cada 10 segundos
}
