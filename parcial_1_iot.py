import network
import urequests
import utime
from machine import ADC, Pin

# Configuración Wi-Fi
SSID = "Arriba1"
PASSWORD = "Internetarriba1"

# Configuración del sensor LM35
sensor = ADC(Pin(26))  # GP26 (ADC0)

# Configuración de ThingSpeak
API_URL = "https://api.thingspeak.com/update?api_key=QWTDPJA0P7HZGJ01&field1="
INTERVALO_ENVIO = 20  # Segundos

# Conectar a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Conectando a Wi-Fi...")
        utime.sleep(1)
    print("Conectado a Wi-Fi", wlan.ifconfig())

# Leer temperatura del LM35
def leer_temperatura():
    valor_adc = sensor.read_u16()  # Leer valor de 16 bits
    voltaje = valor_adc * 3.3 / 65535  # Convertir a voltaje (3.3V referencia)
    temperatura = voltaje * 100  # LM35: 10mV/°C
    return round(temperatura, 2)

# Enviar datos a ThingSpeak
def enviar_datos(temperatura):
    url = API_URL + str(temperatura)
    try:
        respuesta = urequests.get(url)
        print("Datos enviados: Temperatura =", temperatura, "°C. Respuesta:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)

# Programa principal
conectar_wifi()
while True:
    temp = leer_temperatura()
    enviar_datos(temp)
    utime.sleep(INTERVALO_ENVIO)
