# Curso de Web Scraping: Extracción de Datos en la Web

## **Modulo II - HTML: Requests y BeautifulSoup**
- [Clase 4 Descargando una página web](#4-descargando-una-página-web)



# 4. **Descargando una página web**

## Parsing Pagina12

En este módulo veremos cómo utilizar las bibliotecas `requests` y `bs4` para programar scrapers de sitios HTML es decir, sitios estaticos. Nos propondremos armar un scraper de noticias del diario [www.pagina12.com.ar](http://www.pagina12.com.ar/)

Supongamos que queremos leer el diario por internet. Lo primero que hacemos es abrir el navegador, escribir la URL del diario y apretar `Enter` para que aparezca la página del diario. Lo que ocurre en el momento en el que apretamos `Enter` es lo siguiente:

1. El navegador envía una solicitud a la URL pidiéndole información.
2. El servidor recibe la petición y procesa la respuesta.
3. El servidor envía la respuesta a la IP de la cual recibió la solicitud.
4. Nuestro navegador recibe la respuesta y la muestra **formateada** en pantalla.

Para hacer un scraper debemos hacer un programa que replique este flujo de forma automática y sistemática para luego extraer la información deseada de la respuesta. 

Utilizaremos `requests` para realizar peticiones y recibir las respuestas y `bs4` para *parsear* la respuesta y extraer la información.

Te dejo unos links que tal vez te sean de utilidad:

- [Códigos de status HTTP](https://developer.mozilla.org/es/docs/Web/HTTP/Status)
- [Documentación de requests](https://requests.kennethreitz.org/en/master/)
- [Documentación de bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Antes de seguir necesitamos instalar las siguientes librerías:

- jupyter
- requests
- bs4


> 💡 iniciamos nuestro entorno virtual, e instalamos.


```python
# importamos la biblioteca requests
import requests

#guardamos la URL en una variable
url='https://www.pagina12.com.ar/'

# generamos una solicitud a nuestra URL y guardamos el resultado
p12 = requests.get(url)

# verificamos si salio todo bien
p12.status_code
    # Respuestas informativas (100–199),
    # Respuestas satisfactorias (200–299),
    # Redirecciones (300–399),
    # Errores de los clientes (400–499),
    # y errores de los servidores (500–599).

# ver el contenido
print(p12.text)

#Buscar un título en el texto
#Muchas veces la respuesta a la solicitud puede ser algo que no sea un texto: una imagen, un archivo de audio, un video, etc.
p12.content

#Analicemos otros elementos de la respuesta. Encabezados de la respuesta
#vamos a ver el encabezado de la respuesta
p12.headers

#encabezado de la solicitud que hacemos
# existen paginas webs que al detectar el user-agent con nombre por defecto, bloquean la respuesta, solucion enmascarar el nombre
p12.request.headers

#que metodos utilizamos, existen varios metodos PUT, DELETE etc 
#El contenido de la request que acabamos de hacer está avisando que estamos utilizando la biblioteca requests para python 
#y que no es un navegador convencional. Se puede modificar
p12.request.method

#volver a consultar la URL a quien hicimos la solicitud
# util en caso de que existan redireccionamiento (cuando accedemos a un sitio y este nos redirecciona a otro sitio)
p12.request.url

```

## Resumen

- p12 = requests.get(url) // realiza la solicitud.
- p12.status_code // muestra el código de status HTTP de la respuesta.
- print(p12.text) // muestra el HTML de la página sin formatear.
- p12.content // muestra el contenido de la respuesta, puede ser bytes, imágenes, audio.
- p12.headers // muestra el encabezado de la respuesta.
- p12.request.headers // muestra el encabezado de la solicitud. El contenido de esta request avisa al servidor que se está utilizando requests en python y que no es un navegador convencional. Puede ser modificado.
- p12-request.url // muestra la url a la que se le hizo la solicitud.