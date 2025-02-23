import network
import urequests
import utime
from machine import ADC

# Configuración Wi-Fi
SSID = "Arriba1" 
PASSWORD = "Internetarriba1"

# Configuración del sensor
sensor = ADC(4)

# Configuración de ThingSpeak
API_URL = "https://api.thingspeak.com/update?api_key=QWTDPJA0P7HZGJ01&field1="
INTERVALO_ENVIO = 180

# Conectar a Wi-Fi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    # Mientras no logre conectarse, manda el mensaje
    while not wlan.isconnected():
        print("Conectando a Wi-Fi...")
        utime.sleep(1)
    # Cuando logra conectarse, manda un mensaje notificandolo
    print("Conectado a Wi-Fi", wlan.ifconfig())

# Leer temperatura del LM35
def leer_temperatura():
    valor_adc = sensor.read_u16()  # Leer valor de 16 bits
    voltaje = valor_adc * 3.3 / 65535  # Convertir a voltaje
    # Se obtiene la temperatura usando la fórmula del RP2040
    temperatura = (27-(voltaje-0.706)/0.001721)
    # Se devuelve el valor redondeado obtenido
    return round(temperatura, 2)

# Enviar datos a ThingSpeak
def enviar_datos(temperatura):
    # Se junta la URL de la API con los datosa obtenidos para incluir los datos que deben subirse
    url = API_URL + str(temperatura)
    try:
        # Se lanza la petición a ThingSpeak
        respuesta = urequests.get(url)
        # Se imprime la solicitud
        print("Datos enviados: Temperatura =", temperatura, "°C. Respuesta:", respuesta.text)
        respuesta.close()
    except Exception as e:
        # En caso de error, se comunican el error
        print("Error al enviar datos:", e)


# Programa principal
# Se conecta a internet
conectar_wifi()
while True:
    # Se lee la temperatura
    temp = leer_temperatura()
    # Se sube la temperatura medida
    enviar_datos(temp)
    # Se espera para subir otro dato
    utime.sleep(INTERVALO_ENVIO)
