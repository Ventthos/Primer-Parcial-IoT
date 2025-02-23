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

### Para configurar la ThingSpeak
<ol>
  <li>Iniciar sesión en ThingSpeak</li>
  <li>Ir al apartado de my channels</li>
  <li>Dar clic en el botón "New channel"</li>
  <li>Darle un nombre al canal y al canal número 1 darle el nombre de temperature.</li>
  <li>Dar clic a "save channel".</li>
  <li>Una vez ya en el canal, dar clic en MATLAB Visualization.</li>
  <li>Darle clic a create.</li>
  <li>En el apartado de MATLAB code, pegar el código dado en el archivo average.py, cambiando la variable channelID y alertAPIKey por las propias.</li>
  <li>Dar clic en el botón de "save".</li>
  <li>Ir de vuelta al canal creado.</li>
  <li>Dar clic en el botón de MATLAB analysis.</li>
  <li>Pegar el código del archivo email.py en el apartado de MATLAB code.</li>
  <li>Dar clic en el apartado de "React"</li>
  <li>Copiar la siguiente configuración</li>
  ![Configutation](https://github.com/user-attachments/assets/360bd4df-7a04-4925-bd14-e4d12f231efa)
  <li>Dar clic en "save react".</li>
  <li>Presionar "save" en el analysis.</li>

</ol>

### Para configurar la Raspberry
<ol>
  <li>Clonar el repositorio con ayuda de la terminal o alguna aplicación. </li>
  <li>Abrir el IDE Thonny.</li>
  <li>Abrir el archivo parcial_1_iot.py en el IDE.</li>
  <li>Cambiar las variables SSID, PASSWORD y API_URL, por el nombre del internet local, su contraseña y el URL de método GET que se obtiene al crear el canal.</li>
  <li>Conectar la placa a un puerto de la computadora.</li>
  <li>Checar que en apartado inferior derecho diga Micropython(Raspberry pi pico), de lo contrario, dar clic en ese apartado-> configurar intérprete -> Micropython</li>
  <li>Dar clic en el apartado de file -> save as</li>
  <li>Seleccionar Raspberry pi pico.</li>
  <li>Guardar el archivo como main.py</li>
  <li>Desconectar la placa y volverla a conectar.</li>
</ol>


