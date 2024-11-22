import network
import time
import machine
import dht
from umqtt.simple import MQTTClient
import random

# Configurações Wi-Fi
SSID = "Wokwi-GUEST"  # Nome da rede Wi-Fi
PASSWORD = ""         # Senha do Wi-Fi

# Configurações MQTT
MQTT_SERVER = "broker.hivemq.com"  # Substitua pelo seu broker preferido
MQTT_PORT = 1883                  # Ou 8883 para SSL
MQTT_CLIENT_ID = "ESP32Client"    # Nome do cliente MQTT
MQTT_TOPIC_CONSUMO = b"casa/energia/consumo"
MQTT_TOPIC_TEMPERATURA = b"casa/energia/temperatura"

# Definição dos pinos
LDR_PIN = 34  # Pino para o sensor LDR
DHT_PIN = 15  # Pino para o sensor DHT22

# Inicializa o sensor DHT22
dht_sensor = dht.DHT22(machine.Pin(DHT_PIN))

# Configuração Wi-Fi e MQTT
wifi = network.WLAN(network.STA_IF)
mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, port=MQTT_PORT)

# Função para conectar ao Wi-Fi
def connect_wifi():
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)
    print("Conectando ao WiFi...")
    
    while not wifi.isconnected():
        time.sleep(0.5)
        print(".", end="")
    print("\nWiFi conectado!")

# Função para conectar ao MQTT
def connect_mqtt():
    while True:
        try:
            mqtt_client.connect()
            print("Conectado ao broker MQTT!")
            break
        except Exception as e:
            print("Falha na conexão MQTT, tentando novamente em 5 segundos...")
            time.sleep(5)

# Função para verificar e reconectar ao Wi-Fi
def check_and_reconnect_wifi():
    if not wifi.isconnected():
        print("Reconectando ao WiFi...")
        connect_wifi()

# Função para verificar e reconectar ao MQTT
def check_and_reconnect_mqtt():
    try:
        mqtt_client.ping()
    except Exception:
        print("Reconectando ao MQTT...")
        connect_mqtt()

# Função segura para publicar mensagens no MQTT
def safe_publish(topic, message):
    try:
        mqtt_client.publish(topic, message)
    except Exception as e:
        print("Erro ao publicar no MQTT:", e)
        check_and_reconnect_mqtt()

# Função principal
def main():
    connect_wifi()
    connect_mqtt()

    while True:
        check_and_reconnect_wifi()
        check_and_reconnect_mqtt()

        # Leitura do sensor LDR
        ldr_value = machine.ADC(machine.Pin(LDR_PIN)).read()
        consumo_simulado = (ldr_value / 4095) * 100  # Consumo em watts simulados
        consumo_str = "{:.1f}".format(consumo_simulado)
        
        # Leitura do sensor DHT22
        num = random.randint(5,10)
        try:
            dht_sensor.measure()
            temperatura = dht_sensor.temperature()
            temperatura += num
            temp_str = "{:.1f}".format(temperatura)
        except OSError:
            print("Falha na leitura do DHT22!")
            continue

        # Publica o consumo e temperatura no MQTT
        safe_publish(MQTT_TOPIC_CONSUMO, consumo_str)
        safe_publish(MQTT_TOPIC_TEMPERATURA, temp_str)

        print("Consumo (simulado): {} W".format(consumo_str))
        print("Temperatura: {} °C".format(temp_str))
        
        time.sleep(5)  # Intervalo de 5 segundos entre leituras

# Executa o programa
if __name__ == "__main__":
    main()