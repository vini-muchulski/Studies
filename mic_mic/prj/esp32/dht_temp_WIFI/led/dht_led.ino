#include <DHT.h>

#define DHTPIN 26 // Define o pino onde o sensor DHT está conectado
#define DHTTYPE DHT11 // Define o tipo de sensor DHT

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Configurações iniciais
  dht.begin();
  pinMode(15, OUTPUT);
  delay(2000);

  Serial.begin(115200);
}

void loop() {
  // Leitura da temperatura e umidade
  float temp = dht.readTemperature();
  float umidade = dht.readHumidity();

  // Verifica se a leitura foi bem-sucedida
  if (isnan(temp) || isnan(umidade)) {
    Serial.println("Falha ao ler do sensor DHT!");
    return;
  }

  // Liga o pino 15
  digitalWrite(15, HIGH);

  // Exibe as leituras no monitor serial
  Serial.print("TEMP C: ");
  Serial.print(temp);
  Serial.print(" -- Umidade: ");
  Serial.print(umidade);
  Serial.println(" % ");

  // Aguarda 3 segundos
  delay(3000);

  // Desliga o pino 15
  digitalWrite(15, LOW);

  // Aguarda mais 3 segundos
  delay(3000);
}
