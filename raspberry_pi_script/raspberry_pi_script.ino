/******************************************************
 * ESP32 – Accurate Water Quality Monitoring System
 * Sensors: pH, TDS, Turbidity, DS18B20 Temperature
 * Outputs: pH, TDS (ppm), Turbidity (NTU), Temp (°C),
 *          Hardness (ppm)
 * Author: Aryan & ChatGPT | Final Version
 ******************************************************/

#include <OneWire.h>
#include <DallasTemperature.h>

// === PIN CONFIGURATION ===
#define PH_PIN        35
#define TDS_PIN       34
#define TURBIDITY_PIN 33
#define ONE_WIRE_BUS  25    // DS18B20 data pin

// === OBJECTS ===
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);

// === CALIBRATION VALUES ===
float phCalibrationOffset = 0.00;      // adjust after calibration
float tdsCalibrationFactor = 1.0;      // adjust using real TDS meter
float turbidityCalibrationFactor = 1.0; // adjust with known NTU sample

// === GLOBAL VARIABLES ===
float phValue, tdsValue, turbidityValue, temperatureC;
float hardnessPPM;
float voltage;

// === FUNCTIONS ===

// ---- pH Calculation ----
float readPH() {
  int phADC = analogRead(PH_PIN);
  float voltage = phADC * (3.3 / 4095.0);
  float ph = 7 + ((2.5 - voltage) / 0.18) + phCalibrationOffset; // typical pH circuit formula
  return constrain(ph, 0.0, 14.0);
}

// ---- TDS Calculation ----
float readTDS(float tempC) {
  int tdsADC = analogRead(TDS_PIN);
  float voltage = tdsADC * (3.3 / 4095.0);
  float compensationCoefficient = 1.0 + 0.02 * (tempC - 25.0);  // temperature compensation
  float compensatedVoltage = voltage / compensationCoefficient;
  float tds = (133.42 * compensatedVoltage * compensatedVoltage * compensatedVoltage
             - 255.86 * compensatedVoltage * compensatedVoltage
             + 857.39 * compensatedVoltage) * tdsCalibrationFactor;
  return constrain(tds, 0.0, 1000.0); // ppm
}

// ---- Turbidity Calculation ----
float readTurbidity() {
  int turbADC = analogRead(TURBIDITY_PIN);
  float voltage = turbADC * (3.3 / 4095.0);
  float ntu = (voltage * 3000 / 4.5) * turbidityCalibrationFactor;
  return constrain(ntu, 0.0, 1000.0);
}

// ---- Hardness Calculation in ppm ----
// Empirical relation: Hardness ≈ 0.6 × TDS
float calculateHardnessPPM(float tds) {
  return tds * 0.6;
}

void setup() {
  Serial.begin(115200);
  tempSensor.begin();
  delay(2000);
  Serial.println("🚀 ESP32 Water Quality Monitoring Started...");
}

void loop() {
  // === Temperature ===
  tempSensor.requestTemperatures();
  temperatureC = tempSensor.getTempCByIndex(0);
  if (temperatureC == DEVICE_DISCONNECTED_C) temperatureC = 25.0;

  // === Sensor Readings ===
  phValue        = readPH();
  tdsValue       = readTDS(temperatureC);
  turbidityValue = readTurbidity();

  // === Hardness in ppm ===
  hardnessPPM = calculateHardnessPPM(tdsValue);

  // === Combine into Output String ===
  String dataString = "pH:" + String(phValue, 2) +
                      ",TDS:" + String(tdsValue, 0) + " ppm" +
                      ",Turbidity:" + String(turbidityValue, 0) + " NTU" +
                      ",Temp:" + String(temperatureC, 1) + " C" +
                      ",Hardness:" + String(hardnessPPM, 0) + " ppm";

  // === Send via Serial to Raspberry Pi ===
  Serial.println(dataString);

  delay(2000); // 2 seconds interval
}
