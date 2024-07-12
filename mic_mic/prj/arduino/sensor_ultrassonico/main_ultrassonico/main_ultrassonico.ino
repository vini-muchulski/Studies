// Define os pinos do sensor
const int trigPin = 7;
const int echoPin = 6;

// Define variáveis para armazenar o tempo de duração do pulso
long duration;
int distance;

void setup() {
  // Inicializa os pinos
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Inicializa a porta serial
  Serial.begin(9600);
}

void loop() {
  // Gera um pulso de 10µs no pino de trigger
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Mede o tempo de duração do pulso de eco
  duration = pulseIn(echoPin, HIGH);

  // Calcula a distância em centímetros
  distance = duration * 0.034 / 2;

  // Exibe a distância no monitor serial
  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Aguarda um curto intervalo antes da próxima leitura
  delay(1000);
}
