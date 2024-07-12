#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

const char* ssid = "Starlink"; // "SUA_REDE_WIFI"
const char* password = "diversao"; // "SUA_SENHA"

DHT dht(26, DHT11);

void setup() {
  dht.begin();
  
  delay(2000);
  pinMode(15, OUTPUT);

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
    http.begin("http://192.168.0.106:8080");  // Substitua pelo IP do seu servidor
    http.addHeader("Content-Type", "application/json");

    char json_buffer[100];

    float humidity = dht.readHumidity();
    float temp = dht.readTemperature();

    if (isnan(humidity) || isnan(temp)) {
      Serial.println("Falha ao ler do sensor DHT!");
      return;
    }

    // Formatação do JSON
    snprintf(json_buffer, sizeof(json_buffer), "{\"temperature\": %.2f, \"humidity\": %.2f}", temp, humidity);

    Serial.println(json_buffer);

    int httpResponseCode = http.POST(json_buffer);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);
      digitalWrite(15, HIGH);
      delay(5000);
      digitalWrite(15, LOW);
    } else {
      Serial.print("Erro no envio, código: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("Não há conexão Wi-Fi disponível. Tentando reconectar...");
    WiFi.disconnect();
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.println("Tentando reconectar ao WiFi...");
    }
    Serial.println("Reconectado ao WiFi");
  }

  delay(1000); 
}
