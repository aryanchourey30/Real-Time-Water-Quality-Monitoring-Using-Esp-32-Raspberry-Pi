import paho.mqtt.client as mqtt
import serial, json, time

# === MQTT Configuration ===
broker = "192.168.1.10"   # Your MQTT broker IP
topic = "water/sensors/raspberry_pi_01"

# === Serial Configuration ===
SERIAL_PORT = "/dev/ttyUSB0"   # Change if needed (e.g. /dev/ttyACM0)
BAUD_RATE = 115200

# === Setup Serial Connection ===
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"[OK] Connected to {SERIAL_PORT}")
except Exception as e:
    print(f"[ERROR] Could not open serial port {SERIAL_PORT}: {e}")
    exit(1)

# === MQTT Setup ===
client = mqtt.Client(client_id="rpi_publisher")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[OK] Connected to MQTT Broker!")
    else:
        print(f"[ERROR] MQTT connection failed, code {rc}")

def on_disconnect(client, userdata, rc):
    print("[WARN] Disconnected from broker, retrying...")
    time.sleep(2)
    try:
        client.reconnect()
    except Exception as e:
        print(f"[ERROR] Reconnect failed: {e}")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

# === Connect to MQTT Broker ===
try:
    client.connect(broker, 1883, 60)
    client.loop_start()
except Exception as e:
    print(f"[ERROR] Failed to connect to broker: {e}")
    exit(1)

print(f"[INFO] Publishing sensor data to '{topic}' on {broker}\n")

# === Main Loop ===
while True:
    try:
        raw = ser.readline()                              # Read raw bytes
        data = raw.decode(errors="ignore").strip()         # Ignore invalid bytes

        if not data or not data.startswith("pH"):          # Skip bad data
            continue

        # Example data: pH:7.12,TDS:230 ppm,Turbidity:120 NTU,Temp:27.5 C,Hardness:138 ppm
        fields = data.split(",")
        readings = {}
        for f in fields:
            if ":" in f:
                key, value = f.split(":", 1)
                readings[key.strip()] = value.strip()

        payload = {
            "sensor": "ESP32",
            "timestamp": time.time(),
            "readings": readings
        }

        # Publish JSON data to MQTT topic
        client.publish(topic, json.dumps(payload))
        print("Published:", json.dumps(payload))

        time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n[EXIT] Stopping publisher.")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(2)

# === Cleanup ===
client.loop_stop()
client.disconnect()
ser.close()
