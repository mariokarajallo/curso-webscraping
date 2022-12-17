# Curso de Web Scraping: Extracción de Datos en la Web

## **Modulo II - HTML: Requests y BeautifulSoup**
- [Clase 4 Descargando una página web](#4-descargando-una-página-web)
- [Clase 5 Parseando HTML con BeautifulSoup](#5-parseando-html-con-beautifulSoup)



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

# 5. Parseando HTML con BeautifulSoup

Beautiful Soup es una librería Python que permite extraer información de contenido en formato HTML o XML. Para usarla, es necesario especificar un parser, que es responsable de transformar un documento HTML o XML en un árbol complejo de objetos Python. 

Esto permite, por ejemplo, que podamos interactuar con los elementos de una página web como si estuviésemos utilizando las herramientas del desarrollador de un navegador.

<img src="./img/m2c2-1.jpg"/>

Luego de una breve introducción continuamos con la clase. Bien, ya obtuvimos el código HTML de la página en la clase anterior. 

En esta clase veremos cómo extraer de él la información deseada.

```python
#Parseamos el codigo HTML
# esta libreria nos permite extraer la informacion que para nosotros es de interes
from bs4 import BeautifulSoup

# separamos el texto largo en pequenas partes para poder identificar
# s-> soup o sopa
s = BeautifulSoup(p12.text, 'lxml')

#para obtener/saber el tipo de dato de nuestra variable 
type(s)

#imprimir s con el metodo "prettify" de manera que tengas una nocion de como esta 
# estructurada la pagina y poder ver de manera jerarquica el DOM
print (s.prettify())

# Buscamos un elemento con el metodo find()
# BeatifulSoup nos devuelve el primer elemento que encuentra que coincida con el parametro
s.find('ul')

```

Primer ejercicio: obtener un listado de links a las distintas secciones del diario.

- DOM: estructura jerárquica, html
- Usar el inspector de elementos para ver dónde se encuentra la información, ayudara a identificar los elementos que deseemos analizar.
- Ojo cuando la página es responsive, debemos tener en cuenta tanto el diseño escritorio como mobil

```python
# Buscamos elementos especificos agregando atributos -> attrs
# Al atributo le pasamos un diccionario {'nombre atributo':'valor que esperamos obtener'}
# utilizamos el metodo find_all() -> para traer TODOS los elementos que coincidan con el parametro que estamos pasando -> 'li'
s.find('ul',attrs={'class':'horizontal-list main-sections hide-on-dropdown'}).find_all('li')
#como resultado nos devuelve una lista []
```