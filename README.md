# Primer-Parcial-IoT
## Descripción del proyecto
Se trata de un proyecto universitario que tiene el objetivo de medir la temperatura ambiente mediante un sensor LM35 y subir los datos a la plataforma de ThingSpeak gracias a la conexión a internet de una placa Raspberry Pi Pico W.
Debido a ciertos problemas con el sensor ya mencionado, en este repositorio se optó por reemplazarlo por el sensor interno de la Raspberry Pi Pico W, cuyo valor se puede obtener a través del pin ADC 4.

Los datos recolectados y subidos a la plataforma, se muestran en una gráfica y también se analizan con el fin de hacer dos acciones:
<ul>
  <li>Obtener el promedio de los últimos 10 datos y mostrar el historial en una gráfica.</li>
  <li>Mandar un correo electrónico cada vez que la última medición de temperatura tomada superere los 35°C.</li>
</ul>

## Instrucciones de instalación
Para poder replicar el proyecto, se requiere tener:
<ul>
  <li>Una Raspberry Pi Pico w con micro python instalado. </li>
  <li>El IDE Thonny instalado.</li>
  <li>Cable micro USB.</li>
  <li>Una cuenta de ThingSpeak.</li>
  <li>Terminal de Github o aplicación manejadora de Github.</li>
</ul>

### Para configurar ThingSpeak
<ol>
  <li>Iniciar sesión en ThingSpeak.</li>
  <li>Ir al apartado de <strong>My Channels</strong>.</li>
  <li>Hacer clic en el botón <strong>"New Channel"</strong>.</li>
  <li>Asignar un nombre al canal y, en el <strong>Campo 1</strong>, nombrarlo <strong>"Temperature"</strong>.</li>
  <li>Hacer clic en <strong>"Save Channel"</strong>.</li>
  <li>Dentro del canal creado, ir a la pestaña <strong>MATLAB Visualization</strong>.</li>
  <li>Hacer clic en <strong>"Create"</strong>.</li>
  <li>En el apartado <strong>MATLAB Code</strong>, pegar el código del archivo <code>average.py</code>, asegurándose de reemplazar las variables <code>channelID</code> y <code>alertAPIKey</code> con las propias.</li>
  <li>Hacer clic en el botón <strong>"Save"</strong>.</li>
  <li>Volver al canal creado.</li>
  <li>Hacer clic en el botón <strong>MATLAB Analysis</strong>.</li>
  <li>Pegar el código del archivo <code>email.py</code> en el apartado <strong>MATLAB Code</strong>.</li>
  <li>Hacer clic en la pestaña <strong>"React"</strong>.</li>
  <li>Configurar los parámetros según la siguiente imagen:</li>
  <img src="https://github.com/user-attachments/assets/360bd4df-7a04-4925-bd14-e4d12f231efa" alt="Configuración">
  <li>Hacer clic en <strong>"Save React"</strong>.</li>
  <li>Presionar <strong>"Save"</strong> en el análisis.</li>
</ol>

### Para configurar la Raspberry Pi
<ol>
  <li>Clonar el repositorio mediante la terminal o una aplicación de control de versiones.</li>
  <li>Abrir el IDE <strong>Thonny</strong>.</li>
  <li>Abrir el archivo <code>parcial_1_iot.py</code> en el IDE.</li>
  <li>Modificar las variables <code>SSID</code>, <code>PASSWORD</code> y <code>API_URL</code>, reemplazándolas con el nombre de la red WiFi, su contraseña y la URL del método <strong>GET</strong> generada en <strong>ThingSpeak</strong>.</li>
  <li>Conectar la placa a un puerto USB de la computadora.</li>
  <li>Verificar que en la esquina inferior derecha de <strong>Thonny</strong> aparezca <strong>"MicroPython (Raspberry Pi Pico)"</strong>. Si no es así, hacer clic en ese apartado y seleccionar <strong>"Configurar intérprete" -> "MicroPython"</strong>.</li>
  <li>Hacer clic en el apartado <strong>File -> Save As</strong>.</li>
  <li>Seleccionar <strong>Raspberry Pi Pico</strong> como destino.</li>
  <li>Guardar el archivo con el nombre <code>main.py</code>.</li>
  <li>Desconectar y volver a conectar la placa.</li>
</ol>

