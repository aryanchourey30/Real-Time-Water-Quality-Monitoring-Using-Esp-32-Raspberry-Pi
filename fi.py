import paho.mqtt.client as mqtt
import serial, json, time

broker = "192.168.1.10"   # Your broker's IP
topic = "water/sensors/raspberry_pi_01"

# Initialize serial connection (change port if needed)
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Create MQTT client (modern syntax)
client = mqtt.Client(client_id="rpi_publisher")

# If you enabled authentication in Mosquitto, uncomment and edit:
# client.username_pw_set("myuser", "mypassword")

# Define callbacks (optional, for debugging)
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[OK] Connected to MQTT Broker!")
    else:
        print(f"[ERROR] Connection failed with code {rc}")

def on_disconnect(client, userdata, rc):
    print("[WARN] Disconnected from broker, reconnecting...")
    try:
        client.reconnect()
    except:
        time.sleep(2)

client.on_connect = on_connect
client.on_disconnect = on_disconnect

# Connect to broker
client.connect(broker, 1883, 60)
client.loop_start()

print(f"[INFO] Publishing to {broker} on topic '{topic}'")

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                payload = {"sensor": "ESP32", "data": data, "timestamp": time.time()}
                client.publish(topic, json.dumps(payload))
                print("Published:", payload)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\n[EXIT] Stopping publisher.")
    client.loop_stop()
    client.disconnect()
ser.close()