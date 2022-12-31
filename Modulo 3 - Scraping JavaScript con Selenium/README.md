# Curso de Web Scraping: Extracción de Datos en la Web

# **Modulo III - Scraping JavaScript con Selenium**
- [Clase 11 Instalación y configuración de Selenium](#11-instalación-y-configuración-de-selenium)
- [Clase 12 Sitios dinámicos y Selenium](#12-sitios-dinámicos-y-selenium)
- [Clase 13 Selección de elementos](#13-selección-de-elementos)

# 11. **Instalación y configuración de Selenium** 

Para poder utilizar Selenium con Python hay que seguir una serie de pasos que están detallados a continuación.

De todas formas, siempre es recomendable leer la [documentación oficial](https://selenium-python.readthedocs.io/installation.html) de las herramientas.

1. Instalar los bindings de Selenium para Python. Éstos nos permitirán controlar un navegador desde el código.

Ejecutar:

```python
pip install selenium
```

O si estás utilizando Anaconda, puedes instalarlo con:

```python
conda install -c conda-forge selenium
```

**usando Anaconda:** Habrá que installar también el soporte para `chromedriver`  si deseas utilizar Chrome:

```python
conda install -c conda-forge python-chromedriver-binary
```

1. Selenium necesita un driver para poder generar una interfaz con el navegador. Dependiendo el navegador que uses, deberás descargar un driver distinto. Acá te dejo un listado de los links de descarga para los distintos navegadores. Asegurate de descargar el que corresponda con la versión de tu navegador:
- Chrome: [https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Edge: [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- Firefox: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
- Safari: [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

>Es importante que el archivo descargado esté en una carpeta accesible desde la Jupyter Notebook, ya que necesitaremos referenciarlo desde el código para poder utilizarlo.

### Visual Studio - Windows

- Instalar la extensión de Python → Proporciona características **(IntelliSense  (Pylance), Linting, Depuración (multiproceso, remoto), Jupyter Notebooks, formato de código, refactorización, pruebas unitarias).**
- Instalar la extension de Jupyter Notebook
- Crear el ENVIROMENT e instalar las siguientes librerias
    - revisar anotaciones anteriores respecto a la creacion de ENV y Asegúrese de haber seleccionado la versión correcta del intérprete de Python, presionando las teclas **ctrl+shift+P** -> **Python select** **interpreter** , si hay varias versiones de python instaladas.
    - Beatyfull soup → `pip install beautifulsoup4`
    - Requets → `pip install requests`
    - Selenium → `pip install selenium`
    - Una vez que se haya instalado Selenium, verifíquelo con el comando`pip show selenium"`
    - webdriver-manager → `pip install webdriver-manager`
---
Si usas WSL y quieres usar Selenium, En la web no hay muchos tutoriales o guías que te expliquen como se usa Selenium en un Windows Subsystem for Linux (WSL). Es necesario tener instalado o Anaconda o miniconda, que es la versión más simple de Anaconda en la cual tú instalas los packages que necesitas y no los que traen por defecto Anaconda, es mucho más liviana y cumple la misma función. Si quieres una guia más detallada te dejo esta:  [https://towardsdatascience.com/setting-up-a-data-science-environment-using-windows-subsystem-for-linux-wsl-c4b390803dd?gi=287a9058209d](https://platzi.com/clases/1751-webscraping/24799-instalacion-y-configuracion-de-selenium/url).
1. Estando ya en conda te saldrá algo como esto:

```
(base) curso_web_scraping:
```

Lo importante de lo anterior es fijarse que si tienes un base en tu terminal, quiere decir que ya tienes conda.

2. Aquí puedes crear un environment nuevo y puedes llamarlo como quieras, si quieres saber como te dejo este cheatsheet: [https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf](https://platzi.com/clases/1751-webscraping/24799-instalacion-y-configuracion-de-selenium/url)

3. Selenium para su funcionamiento usa el driver del navegador que tú uses, ya sea Chrome, Firefox, etc. En mi caso uso Firefox que he visto que tiene muy pocos tutoriales para Selenium, pero esta guía te servirá para los demás navegadores. Lo descargas como te señala la guía de arriba, es importante que descargues la versión para Windows ya sea de 32 o 64 bits dependiendo de tu computador. Este te descargará un comprimido con el Driver.

4. Si usas VSCode es importante que instales la extensión de Python que está en la marketplace. Aquí es importante elegir como tu interpreter path donde tengas instalado tu conda: Por defecto en WSL se instala en el home denotado por **~**, aquí eliges **~/miniconda3/bin/python**. No te preocupes esta ruta la puedes modificar las veces que quieras y usar la que quieras, siempre y cuando sea una que este Python.

5. Vas a ir al directorio en que vas a trabajar y usar Selenium, en ese directorio vas a descomprimir la carpeta zip del driver y te dejara un **.exe**, en mi caso **geckodriver.exe**. Es importante que lo tengas en la misma carpeta en que vas a crear tu **.py**.

6. Ahora vas a probar que selenium funcione: crea un archivo test_selenium.py (o como quieras llamarlo) y vas a ingresar las siguientes líneas de código.

```
from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver.exe')
driver.get('https://www.google.com')
driver.close()
```

Si tu navegador es Chrome solo cambia el Firefox por Chrome y adentro de los paréntesis le dirás que hay una ruta ejecutable, aquí tendrás que recordar las rutas relativas y absolutas en Linux. Recuerda que ./ significa que el ejecutable está en el directorio que estás trabajando,el current directory.

7. Luego ejecutaras el código:

```
python3 test_selenium.py
```

De esta manera se te abrirá el navegador, ingresara [https://www.google.com](https://www.google.com/) y luego lo cerrara automáticamente. Aquí empieza la magia.

Si no les funciona dejo otra opcion: los links de otros tutoriales:

[https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/](https://www.gregbrisebois.com/posts/chromedriver-in-wsl2/)[https://blog.henrypoon.com/blog/2020/09/27/running-selenium-webdriver-on-wsl2/](https://blog.henrypoon.com/blog/2020/09/27/running-selenium-webdriver-on-wsl2/)[https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/](https://seanthegeek.net/234/graphical-linux-applications-bash-ubuntu-windows/)

Este video por si a alguien le sirve [https://www.youtube.com/watch?v=qYqGGrAA_IA&ab_channel=NicolasAlvarez](https://www.youtube.com/watch?v=qYqGGrAA_IA&ab_channel=NicolasAlvarez)

### Miniconda - Conda (windows)

- Iniciar Anconda Prompt
- Una vez abierto la terminal podemos ver si tenemos instalado python y donde
    - $ where python
- Una vez que nos aseguramos que tenemos instalado python, creamos nuestro variable de entorno, para instalar las librerias que necesitaremos para este proyecto y no afecte a otros futuros proyectos
    - `$ conda create -n myenv`
    - para iniciar → `$ conda activate myenv`
    - desactivar → `$ conda deactivate`
- ahora instalamos las librerias en nuestra variable de entorno activada
    - `$ pip freeze` → podemos ver todas las librerias instaladas y disponibles
    - `$ python -m pip install --upgrade pip` → para instalar actualizaciones de pip en windows
    - `$ pip install nombre_libreria` → para instalar las librerias que necesitemos
    - Beatyfull soup → `pip install beautifulsoup4`
    - Requets → `pip install requests`
    - Selenium → `pip install selenium`
    - Una vez que se haya instalado Selenium, verifíquelo con el comando`pip show selenium"`
    - webdriver-manager → `pip install webdriver-manager`


### Documentacion

[Xpath cheatsheet](https://devhints.io/xpath)

[The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)

[Selenium with Python - Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/index.html)

# 12. **Sitios dinámicos y Selenium** 
Selenium es una herramienta que nos permitirá controlar un navegador y podremos utilizar las funcionalidades del motor de JavaScript para cargar el contenido que no viene en el HTML de la página. Para esto necesitamos el módulo `webdriver`.

```python
from selenium import webdriver
```

## Instalar Selenium y webdriver-manager:

## Configure los controladores web automáticamente

---

Necesitamos controladores web para diferentes navegadores web. Podemos configurar usando dos opciones.

- **Descargue el controlador web binario** , descomprima y configure, y **[manualmente](https://devenum.com/how-to-install-selenium-on-windows-python/)** Descargamos manualmente el binario del controlador web y lo descomprimimos en algún lugar del sistema y configuramos la ruta. ¡¡¡Es tedioso!!! Además de eso, cada vez que se lanza la nueva versión del controlador, debe repetir todos los pasos una y otra vez.
- **Automáticamente, siguiendo los pasos a continuación** Estando en 2022 ya no es necesario descargar el `webdriver` de manera manual. Dado que ejecutable path está `deprecated` descontinuado, hay que instalar la librería “`webdriver-manager`” que te descarga automáticamente el webdriver y te lo guarda en cache. En lugar de instalar cada controlador web por separado y configurar la ruta manualmente. El administrador de controladores web lo maneja solo.
    - El primer paso es instalar el administrador de controladores web usando el comando "`pip install web driver-manager`" y usarlo para los diferentes navegadores web.

### **Automatice la instalación y actualización del navegador Chrome**

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://google.com")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.quit()
```

iniciando modo incógnito

```python
#para google chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--incognito')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

```

### **Automatice la actualización e instalación del navegador Firefox**

```python
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
 
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
 
driver.maximize_window()
driver.get("https://google.com")
print('driver Title:',driver.title)
print('Driver name:',driver.name)
print('Driver URL:',driver.current_url)
driver.quit()
```

si alguien usa Firefox en Linux, y tiene problemas puede probar este método, primero instale: `geckodriver-autoinstaller`

```python
pip install geckodriver-autoinstaller
```

Y luego usar el siguiente código:

```python
from selenium import webdriver
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()
# Check if the current version of geckodriver exists,
# and if it doesn't exist, download it automatically,
# then add geckodriver to path.

driver = webdriver.Firefox()
driver.get(url)
```

### Navegador Microsoft Edge:

```python
#para el caso para Microsoft Edge:
from selenium import webdriver
from selenium.webdriver.edge.service import Service
#Pueden installar webdriver_manager con pip
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#Para abrir Edge en modo incógnito
options = webdriver.EdgeOptions()
options.add_argument('-inprivate')
#Instanciar el driver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()),options=options)
```

### Mac OS 2022

Arreglando error:  *“chromedriver” cannot be opened because the developer cannot be verified. Unable to launch the chrome browser on Mac OS*

xattr -d com.apple.quarantine <PATH-TO-CHROMEDRIVER>

Sugerencia

- instalar con brew install chromedriver
- obtener path con which chromedriver
- obtendrás algo como “/usr/local/bin/chromedriver”, luego xattr -d com.apple.quarantine /usr/local/bin/chromedriver lo que removerá de la “cuarentena” al driver

### Selenium para Deepnote o Google Colab

Si estás trabajando en la nube, no podrás acceder al driver que hayas instalado en local desde las máquinas virtuales remotas. Pero hay solución.

Básicamente, debes descargar los drivers en tu máquina virtual y configurar para que no muestren la interfaz gráfica del navegador. 

Te  dejo los enlaces de los tutoriales para hacerlo.

- Deepnote:
    - Accede acá: [https://deepnote.com/@joshzwiebel/Custom-Datasets-with-Selenium-and-XPath-CYA2QRnkTbWQYqDQ2v36KQ](https://deepnote.com/@joshzwiebel/Custom-Datasets-with-Selenium-and-XPath-CYA2QRnkTbWQYqDQ2v36KQ)
- Google Colaboratory:
    - Creo que podrías hacer lo mismo que se hace en Deepnote. Yo no lo he probado aún. Pero te dejo un tutorial (diferente) de alguien que ya le funcionó.
    - Accede acá: [https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com](https://stackoverflow.com/questions/51046454/how-can-we-use-selenium-webdriver-in-colab-research-google-com)
    - Cabe recalcar que esto también lo puedes hacer en local para Linux (o WSL) y que, de hecho, podría resultar más eficiente al no usar interfaces gráficas.

### Otras Recomendaciones

- Es recomendable que descargues el controlador del explorador que utiliza Jupyter Notebook para hacer launch
- Si utilizas Anaconda puedes ahorrarte muchos problemas simplemente yendo a “Environments” e instalar directo selenium
- En Safari debes de seguir las instrucciones que vienen en la [página web](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) :
1. Asegúrese de que el menú Desarrollar esté disponible. Se puede activar abriendo las preferencias de Safari (Safari > Preferencias en la barra de menús), yendo a la pestaña Avanzado y asegurándose de que la casilla de verificación Mostrar menú Desarrollar en la barra de menús esté marcada.
2. Habilitar Automatización Remota en el menú Desarrollar. Esto se hace a través de Desarrollar > Permitir automatización remota en la barra
de menús.
3. Autorizar safaridriver lanzar el servicio webdriverd. Para permitir esto debes ir a la consola y correr:

```
run /usr/bin/safaridriver --enable
```

Te pedirá que introduzcas tu contraseña de inicio para dar los permisos necesarios.

- Regresando a la clase… Cuando estés corriendo el código en Jupyter Notebook desde **Safari **debes hacer estos cambios:

```python
from selenium import webdriver
url='https://www.latam.com/es_ar/apps/personas/booking?fecha1_dia=25&fecha1_anomes=2019-10&fecha2_dia=12&fecha2_anomes=2019-11&from_city2=MAD&to_city2=BUE&auAvailability=1&ida_vuelta=ida_vuelta&vuelos_origen=Buenos%20Aires&from_city1=BUE&vuelos_destino=Madrid&to_city1=MAD&flex=1&vuelos_fecha_salida_ddmmaaaa=25/10/2019&vuelos_fecha_regreso_ddmmaaaa=12/11/2019&cabina=Y&nadults=1&nchildren=0&ninfants=0&cod_promo='
driver = webdriver.Safari()
driver.get(url)
```

### Anacando → Selenium y webdriver-manager:

1. Abrir Anaconda navigator
2. Abrir CDM.exe Prompt Se debe abrir la consola (ventana de fondo negro)
3. Colocar los siguientes comandos

```python
pip install selenium
pip install webdriver-manager
```

1. Ahora ya se puede volver a trabajar en la Jupyter: Se coloca los siguientes comandos con los que se abre una nuevo navegador

```python
from selenium import webdriver
```

- si queremos utilizar chrome

```python
from webdriver_manager.chrome import ChromeDriverManager
```

- instanciamos nuestro driver

```python
driver = webdriver.Chrome(ChromeDriverManager().install())
```

## Ahora si! despeguemos ✈

Para este proyecto de scraper a la pagina web de Latam AirLines, realizamos la requests. Pero como `son sitios dinámicos` y hacen uso de `Javascript`, en Jupyter notebook, python NO puede procesar este lenguaje y por eso hacemos uso de `Selenium`

<img src="./img/m3c1-1.png"/>

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.latam.com/es_co/apps/personas/booking?fecha1_dia=11&fecha1_anomes=2021-01&fecha2_dia=25&fecha2_anomes=2021-01&from_city2=JFK&to_city2=MDE&auAvailability=1&ida_vuelta=ida_vuelta&vuelos_origen=Medell%C3%ADn&from_city1=MDE&vuelos_destino=Nueva%20York&to_city1=JFK&flex=1&vuelos_fecha_salida_ddmmaaaa=15/11/2020&vuelos_fecha_regreso_ddmmaaaa=30/11/2020&cabina=Y&nadults=2&nchildren=0&ninfants=1&cod_promo=&stopover_outbound_days=0&stopover_inbound_days=0&application=#/'

agent = {"User-Agent":"Mozilla/5.0"}
r = requests.get(url, headers=agent)

r.status_code

s = BeautifulSoup(r.text, 'lxml')

print(s.prettify())
```

Hasta acá accedemos al html pero no a la información que buscamos. Ya que necesitamos interpretar el Javascript. Para ello Implementamos `selenium` 

```python
from selenium import webdriver
```

y la librería para cargar el driver del navegador en el cache

```python
from webdriver_manager.chrome import ChromeDriverManager
```

Declaramos `driver` para ejecutar el driver de selenium, pero antes declaramos `options` y agregamos argumentos, en este caso el argumento para abrir el navegador en modo incógnito.

```python
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
```

Ejecutamos el `driver` y le pasamos la url de la pagina de Latam Airlines

```python
driver.get(url)
```

Para cerrar el navegador

```python
drive.close()
```

---

> 🛠 Tip:  Si haces el request y te sale un status code 403 quiere decir que fue rechazada (busca que es el codigo 403 de HTTP en google).  Esto sucede porque tu User-Agent es el que trae por defecto el modulo requests:


```python
#aqui para ver el codigo de estado
print(response.status_code)
# y aqui podras ver tu user-agent
print(response.request.headers)
```

Te dará como salida/Output (o muy similar):

```
403
{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

```

Solo tienes que modificar este Header usando el User-Agent que usa tu navegador, en mi caso es:

- Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0

Puedes encontrarlo en El inspector de tus dev tools , en el apartado de red (inspector de elementos en el navegador).

Para que te funcione solo modificas el header asi:

```python
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.request.headers)
```

y te dará un Output así:

```
200
{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

```

Si quieres entender el porqué modificando el User-Agent si te da un request con código 200, busca para qué funciona.

En este blog te explica que es User-Agent: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)

Aquí te explica como hacerlo: [https://www.kite.com/python/answers/how-to-make-a-request-with-a-user-agent-in-python](https://www.kite.com/python/answers/how-to-make-a-request-with-a-user-agent-in-python)

---

## Otros ejemplos Resueltos

#### Ejemplo 1

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

try:
    options = webdriver.ChromeOptions ()
    options.add_argument ('--incognito')
    
    ser = Service ("C:\\Users\\Auler\\Downloads\\chromedriver.exe")
    driver = webdriver.Chrome (service = ser, options = options)
    
    driver.get (sitio)
    
except Exception as e:
    print ('Error:')
    print (e)
    print ('\n')
```

#### Ejemplo 2

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)

url = '...'
driver.get(url)```
```

# 13. **Selección de elementos** 
Se recomienda a la hora de inspeccionar paginas web, tener el inspector de elemento en otra ventana separada, para que no afecte la navegación del mismo ya que las paginas web reconocen la resolución del navegador, y acomodan el contenido en función a ello .  

Para buscar y seleccionar uno o varios elementos de la web utilizaremos la función `find_element` o `find_elements` y armar el `xpath` (la ruta XML) que nos va a permitir identificar donde se encuentran cada uno de los elementos que necesitamos extraer a través de los tag y sus atributos.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bc08863a-e210-4aaf-bf82-adfe2bd8495b/Untitled.jpeg)

En la misma documentación Oficial de Selenium obtendremos todo lo necesario para aprender a utilizar la función de `find_element` para un elemento, o para múltiples elementos `find_elements`

[Locating Elements - Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/locating-elements.html)

#### Xpath cheatseeht

[Xpath cheatsheet](https://devhints.io/xpath)

#### introducción a Xpath

[XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

Elementos importantes de Xpath:

```python
"//" busca en todos los hijos del elemento.
"/" busca sólo en hijos directos
"." indica que la búsqueda debe empezar en ese elemento y no en el origen del árbol
Los atributos de los tags se buscan entre [] y con @
```

## ¡Empecemos! ✈

Vamos a scrapear el sitio de Latam para averiguar datos de vuelos en función el origen y destino, fecha y cabina. 

<img src="./img/m3c2-2.png"/>
Vamos a scrapear el sitio de Latam para averiguar datos de vuelos. La información que esperamos obtener de cada vuelo es:
- Horas de salida y llegada (duración)

```python
from selenium import webdriver
#importamos libreria para cargar el driver automaticamente
from webdriver_manager.firefox import GeckoDriverManager
# pagina del vuelo seleccionado ida, fecha, destino
url='https://www.latamairlines.com/ar/es/ofertas-vuelos?origin=ASU&inbound=null&outbound=2022-12-01T15%3A00%3A00.000Z&destination=MAD&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=RECOMMENDED'
```

Paso 1: instanciar un **driver** del navegador (Necesitamos controladores web para diferentes navegadores web, en este ejemplo usamos para firefox. )

```python
options = webdriver.FirefoxOptions()
# Podemos agregarle opciones al driver para utilizar los distintos modos del navegador
options.add_argument('-private')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
```

Paso 2: hacer que el navegador cargue la página web.

```python
driver.get(url)
```
<img src="./img/m3c2-3.png"/>

paso 3: Extraer información de la pagina. Carguemos la página y analicemos dónde se encuentra la información. Vemos que el bloque de vuelos se encuentra en una `ul` y que cada vuelo es un item de la lista, `li`.

<img src="./img/m3c2-4.png"/>

```python
#Usaremos el Xpath para obtener la lista de vuelos
vuelos = driver.find_elements('xpath','//ol/li')
print (vuelos)
```

```
# nos devuelve una lista de objetos selenium
[<selenium.webdriver.remote.webelement.WebElement (session="742d6ba4-917a-4f2b-b3ef-07645908e7c8", element="7ba3e480-987b-4ee7-951e-bdb77af4522b")>, <selenium.webdriver.remote.webelement.WebElement (session="742d6ba4-917a-4f2b-b3ef-07645908e7c8", element="77cd6bbf-6e4c-4b75-b52b-bd969bfe567a")>, <selenium.webdriver.remote.webelement.WebElement (session="742d6ba4-917a-4f2b-b3ef-07645908e7c8", element="003e2b53-f5f1-40a8-ae1e-d95d0148696b")>,
.
.
.]
```

Obtengamos la información de la hora de salida, llegada y duración del vuelo

<img src="./img/m3c2-5.png"/>

```python
#seleccionamos el primer vuelo
vuelo_1=vuelos[0]
#hora de salida
hora_salida=vuelo_1.find_element('xpath','//div[@class="sc-ixltIz dfdfxH flight-information"]/span[1]').text
print (hora_salida)
```

```
10:50
```

```python
#hora de llegada
hora_llegada=vuelo_1.find_element('xpath','.//div[3]/span[1]').text.replace('\n+1','')
print (hora_llegada)
```

```
13:55
```

```python
# Duracion del vuelo
duracion_vuelo= vuelo_1.find_element('xpath','.//div[2]/span[2]').text
print (duracion_vuelo)
```

```
23 h 5 min
```

Paso 4: cerrar el navegador

```python
driver.close()
```

### Otros ejercicios Resueltos


> 🛠 Reto: Obtener fecha de salida, llegada y duración de un vuelo utilizando selenium y Xpath.

Al leer y/o analizar estos ejercicios quizas te pueda ayudar a solucionar algun error que puedas tener en tu propio codigo o ver como otros usuarios resuelven de diferente maneras el mismo problema.

#### Ejercicio 1

```python
from time import sleep
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

URL = "https://connect.avianca.com/flights/CLO/NAP/2022-05-02/2022-09-30/1-adults?res=CO&lang=ES&utm_source=avianca"
wp_url = "https://chat.whatsapp.com/GRYhS6aPodA8vZNwOtcnbb"
XPATH_FLIGHTS = "//*/li[@class='Itinerary']/text()"
FOX = Service(r"C:\Drivers\firefox\geckodriver.exe")

def run_firefox():
    r_url =req.get(URL)
    if r_url.status_code == 200:
        try:       
            opt = wd.FirefoxOptions()
            opt.add_argument("--incognito")
            firefox = wd.Firefox(service=FOX, options=opt)
            firefox.get(URL)
            sleep (5)
            flights = firefox.find_elements(By.XPATH, value="//*/li[@class='Itinerary']")
            print(flights)
        except Exception as erre:
            print("Error: " , "\n", erre)

if __name__ == "__main__":
    run_firefox()
```

#### Ejercicio 2

Tener en cuenta que tuve que sacarle al arrival time un text hijo que decía “+1”. Me costó un montón encontrar la solución a eso, ya que con selenium no es tan fácil. Finalmente lo logré. Además tener en cuenta que uso “contains” para no poner los “id” de las clases, que seguramente van cambiando con el tiempo:

```python
for flight in flights:
    departure_time = flight.find_element(By.XPATH, './/div[contains(@class, "flight-information")][1]/span').text
    flight_duration = flight.find_element(By.XPATH, './/div[contains(@class, "flight-duration")]/span[2]').text
    arrival_time_el = flight.find_element(By.XPATH, './/div[contains(@class, "flight-information")][2]/span')
    arrival_time_child = arrival_time_el.find_element(By.XPATH, './*').text
    arrival_time = arrival_time_el.text.replace(arrival_time_child, '')
    print(f'Departure time: {departure_time}. Flight duration: {flight_duration}. Arrival time: {arrival_time}')
```

#### Ejercicio 3

```python
hora_salida = vuelo.find_element(by=By.XPATH,value='.//div[@class="sc-bEeSwp fYVRJw flight-information"]/span[1]').text
aeropuerto_salida = vuelo.find_element(by=By.XPATH,value='//div[@class="sc-bEeSwp fYVRJw flight-information"]/span[2]').text
duracion_vuelo = vuelo.find_element(by=By.XPATH,value='//div[@class="sc-bEeSwp fYVRJw flight-duration"]/span[2]').text
```

#### Ejercicio 4

```python
from selenium import webdriver

# Cabe resaltar que la carpeta 'webdriver.exe' se encuentra dentro de la carpeta del proyecto local en Jupyter Notebook. 
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
url = 'https://www.latamairlines.com/pe/es/ofertas-vuelos?origin=LIM&inbound=2022-09-26T17%3A00%3A00.000Z&outbound=2022-09-23T17%3A00%3A00.000Z&destination=BOG&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED'

# Conectarse con la página web, en mi caso, me conecté a la página web de Latam Airlines Perú.
driver.get(url)

# Extraer la información de los vuelos
from selenium.webdriver.common.by import By
vuelos = driver.find_elements(by=By.XPATH, value='//li[@class="sc-bJTOcE dnJSKm"]')
vuelo = vuelos[0]

# Dado que la información de la hora de salida y llegada se encuentra en diferentes 'div', pero tienen el mismo nombre de clase, por lo tanto, se debe utilizar el método '.find_elements()' para obtener mencionada información.

tiempo_salida_llegada = vuelo.find_elements(by=By.XPATH, value='.//div[@class="sc-cLxPOX jDdIbe flight-information"]/span[@class="sc-eTyWNx ilRvHO"]')

# Información de la hora de salida
tiempo_salida = tiempo_salida_llegada[0].text

# Información de la hora de llegada
tiempo_llegada = tiempo_salida_llegada[1].text

# Información de la duración del vuelo
duracion_vuelo = vuelo.find_element(by=By.XPATH, value='.//div[@class="sc-cLxPOX jDdIbe flight-duration"]/span[@class="sc-bsVVwV jAgyHF"]').text
```

#### Ejercicio 5

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
s=Service('D:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
url='https://www.latamairlines.com/co/es/ofertas-vuelos?origin=CLO&inbound=2022-09-24T17%3A00%3A00.000Z&outbound=2022-09-23T17%3A00%3A00.000Z&destination=BOG&adt=1&chd=0&inf=0&trip=RT&cabin=Economy&redemption=false&sort=RECOMMENDED'
driver.get(url)
vuelos = driver.find_element("xpath", '//div[@class="sc-ZUflv hlABHQ"]')
print(vuelos)>
```

#### Ejercicio 6

```python
# solucion vieja “DeprecationWarning” Ya no se usa find_elements_by_xpath. selenium actualizo
for flight in flights:
    flight_info = flight.find_elements_by_xpath('.//div[@class="sc-hAXbOi jocxib flight-information"]')
    departure = flight_info[0].find_element_by_xpath('.//span[@class="sc-cfWELz iIRsqM"]').text
    arrival = flight_info[1].find_element_by_xpath('.//span[@class="sc-cfWELz iIRsqM"]').text
    flight_time = flight.find_element_by_xpath('.//span[@class="sc-hCaUpS cTjSBD"]').text
    arrival = arrival.replace('\n', '')
    print(f'Salida:{departure} Llegada:{arrival} Duración:{flight_time}')
```

#### Ejercicio 7

```python
#Solucion vieja “DeprecationWarning” Ya no se usa find_elements_by_xpath. selenium actualizo
def obtener_info_vuelo(vuelo):
    hora_salida, hora_llegada = vuelo.find_elements_by_xpath('.//span[contains(@class, "dFRJGh")]')
    duracion = vuelo.find_element_by_xpath('.//span[contains(@class, "ZOLOQ")]')
    precio = vuelo.find_element_by_xpath('.//span[contains(@class, "displayAmount")]')
    return (hora_salida.text, hora_llegada.text, duracion.text, precio.get_attribute('aria-label'))
```

#### Ejercicio 8

```python
# Solucion vieja “DeprecationWarning” Ya no se usa find_elements_by_xpath. selenium actualizo
for vuelo in vuelos:
    schedule = vuelo.find_elements_by_xpath('.//div[@class="sc-izvnbC eqFECQ flight-information"]/span[@class="sc-gMcBNU gwIRwm"]')
    duration = vuelo.find_element_by_xpath('.//span[@class="sc-iLVFha jrpeUd"]')
    print(f'Salida a: {schedule[0].text}, llega a:  {schedule[1].text} y dura: {duration.text}')
```

## Importante

Si ha ustedes no les sale ningún viaje cuando usan el `Chrome` con Python (webdriver) pero mágicamente usando Chrome normal si salen viajes, es porque Latam ha detectado que estás usando `selenium` y no quiere dejarte ver sus viajes. ¿Cómo solucionar eso?

Añade este código después de `options` al momento de instanciar el driver:

```python
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
```

## Paginas de interés

Como armar tus propios Xpath

[Xpath cheatsheet](https://devhints.io/xpath)

Introducción Selenium

[guru99 - Selenium Tutorial](https://www.guru99.com/selenium-tutorial.html)

[guru99 - What is Selenium? Introduction to Selenium Automation Testing](https://www.guru99.com/introduction-to-selenium.html)

[guru99 - Find Element and FindElements by XPath in Selenium WebDriver](https://www.guru99.com/find-element-selenium.html)