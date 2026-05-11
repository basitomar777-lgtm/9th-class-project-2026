
//VCC - 5V
//GND - GND
//DATA - Digital pin 2

#include <DHT.h>

#define DHTPIN 2        // Digital pin connected to DHT
#define DHTTYPE DHT11   // Change to DHT22 if using DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("DHT Sensor Test");
  dht.begin();
}

void loop() {
  delay(2000);  // Wait 2 seconds between readings

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature(); // Celsius

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" %\t");

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
}
