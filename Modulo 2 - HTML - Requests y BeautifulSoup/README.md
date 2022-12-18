# Curso de Web Scraping: Extracción de Datos en la Web

## **Modulo II - HTML: Requests y BeautifulSoup**
- [Clase 4 Descargando una página web](#4-descargando-una-página-web)
- [Clase 5 Parseando HTML con BeautifulSoup](#5-parseando-html-con-beautifulSoup)
- [Clase 6 Extrayendo información](#6-extrayendo-información)
- [Clase 7 Manejo de errores](#7-manejo-de-errores)



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
# 6. Extrayendo información
Vamos a empezar a extraer información contenida en los tags. A veces puede ser el texto del tag o puede ser algún atributo

>Función que recibe un objeto de BeautifulSoup de una página de una sección y devuelve una lista de URLs a las notas de esa sección

```python
# reto-extrayendo-informacion

import requests
from bs4 import BeautifulSoup
# obtenemos la pagina de donde extraemos la informacion
link_principal='https://www.pagina12.com.ar'
pagina_principal = requests.get(link_principal)

#parseamos la pagina
soup = BeautifulSoup(pagina_principal.text, 'lxml')

#lista vacia para links de notas de secciones
URL=[]

def obtener_notas(soup):
    '''
    Función que recibe un objeto de BeautifulSoup de una página de una sección 
    y devuelve una lista de URLs a las notas de esa sección
    '''
    # Secciones -> creamos un array de todos los elementos con el tag DIV que tengan el atributo class=p12-dropdown-column
    # y seleccionamos nuestro primer elemento
    secciones= soup.find_all('div', attrs={'class':'p12-dropdown-column'})[0]

    #buscamos los tag a para obtener el href que contiene el link de la seccion
    link_secciones= secciones.find_all('a')
    
    #recorremos el array de tag a y obtemos los elementos href que contienen links
    href_link_secciones=[i.get('href') for i in link_secciones]

    #seleccionamos el primer link que corresponde a la seccion el pais
    pagina_seccion_el_pais= requests.get(href_link_secciones[0])
    #parseamos la pagina seccion el pais
    soup_pagina_seccion_el_pais= BeautifulSoup(pagina_seccion_el_pais.text,'lxml')

    #la pagina de articulos de noticias se dividen en 3 sectores
    #Top (1 noticia principal) - Semi(2 noticias semiprincipales) -  articulos (el resto de noticias)

    #!TOP
    top_noticias_seccion_el_pais = soup_pagina_seccion_el_pais.find('div', attrs={'class':'article-item__content'})
# agregamos el link principal + el contenido href dentro del elemento a que se encuentra en nuestro div 
    link_top_noticias_seccion_el_pais= [link_principal + top_noticias_seccion_el_pais.a.get('href')]

    #! Semi
    semi_noticias_seccion_el_pais = soup_pagina_seccion_el_pais.find_all('h2', attrs={'class':'title-list featured-article'})
		#recorremos el array de noticias semi importantes y seleccionamos el valor de href de los h2
    link_semi_noticias_seccion_el_pais=[link_principal+i.a.get('href') for i in semi_noticias_seccion_el_pais]

    # #! articulos
    articulos_noticias_seccion_el_pais= soup_pagina_seccion_el_pais.find_all('h2', attrs={'class':'is-display-inline title-list'})

    link_articulos_noticias_seccion_el_pais=[link_principal+i.a.get('href') for i in articulos_noticias_seccion_el_pais]

    URL.extend(link_top_noticias_seccion_el_pais)
    URL.extend(link_semi_noticias_seccion_el_pais)
    URL.extend(link_articulos_noticias_seccion_el_pais)

    
    return URL

print (obtener_notas(soup))
```

<details>
<summary><b>Otros ejercicios resueltos</b></summary>

_Markdown is valid, but add empty lines to separate from the HTML tags._

- Bullet
- Points

```python
import requests
from bs4 import BeautifulSoup

HOME_URL = 'https://www.pagina12.com.ar'

def parse_page(link):
    try:
        section = requests.get(link)
        if section.status_code == 200:
            pass
            #PARSE CURRENT PAGE
            soupSection = BeautifulSoup(section.text, 'lxml')
            #GET FEATURED ARTICLE
            featuredArticle = soupSection.find('h1', attrs={'class': 'title-list'})
            featuredLink = HOME_URL + featuredArticle.a.get('href')
            #GET HORIZONTAL ARTICLES
            articleListH = soupSection.find_all('h2', attrs={'class': 'title-list featured-article'})
            articleLinkH = [(HOME_URL + titleH.a.get('href')) for titleH in articleListH]
            #GET VERTICAL ARTICLES
            articleListV = soupSection.find_all('h2', attrs={'class': 'is-display-inline title-list'})
            articleLinkV = [(HOME_URL + titleV.a.get('href')) for titleV in articleListV]

            return(articleLinkH + articleLinkV)
        else:
            raise ValueError(f'Error: {section.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            #GET NAV LINKS
            listLinks = soup.find('ul', attrs = {'class': 'main-sections'}).find_all('li')
            link = listLinks[1].a.get('href')
            parse_page(link)
        else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__=='__main__':
    run()
```
```python
def news(link):
    """
    Definición: Extracción de titulares y links de portal de noticias Argentino.
    
    Parámetro: 
    -link: URL de la sección de noticias a procesar.
    
    Retorno: Títulos y links de las noticias pertenecientes a ella.   
    """
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "lxml")
    article_list = soup.find_all("h4", attrs={"class" : "is-display-inline title-list"})
    #Obtenemos los links de las noticias
    links_list = [link[:27]+article.a.get("href") for article in article_list]
    #Obtenemos los titulos de las noticias
    titles_list = [article.a.get_text() for article in article_list]
    return titles_list,links_list
```

```python
#Importacion de Librerias
import requests
from bs4 import BeautifulSoup

#Funciones
def GetLinks(ProtocolDomain, Soup):
    Notices=Soup.find_all('div',{'class','article-item__content'})
    Notices=[ProtocolDomain+ Notice.a.get('href') for Notice in Notices]
    return(Notices)

#Variables de Entrada
Links_sections='https://www.pagina12.com.ar/secciones/el-pais'
url='https://www.pagina12.com.ar'

#Preparacion de Variable
page = requests.get(Links_sections)
soup= BeautifulSoup(page.text,'lxml')

#Invocacion de Funcion
GetLinks(url, soup)
```

```python
# Define una nueva funcion
def obtener_articulos(soup):
    # Crea un array para almacenar los enlaces
    lista_articulos = []
    
    # Busca el div que almacena el primer articulo
    articulo_principal = soup.find('div', attrs={'class':'article-item__content'})
    if articulo_principal:
        # Agrega el href del a que esta dentro del h2 
        lista_articulos.append(articulo_principal.h2.a.get('href'))
    
    # Busca todos los divs que almacenan articulos
    grupo_articulos = soup.find_all('div', attrs={'class':'articles-list'})
    # Hay dos grupos de articulos, dos semi featured, yel resto de los articulos
    # Esta iteracion hace un loop por los grupos de articulos
    for grupo in grupo_articulos:
        articulos = grupo.find_all('article', attrs={'class':'article-item'})
        
        # Y esta hace un loop entre los articulos dentro de ese grupo de articulos
        for articulo in articulos:
            # Busca el div que almacena el texto, aunque el href tambien se podria conseguir enla img
            contenedor = articulo.find('div', attrs={'class':'article-item__content-footer-wrapper'})
            # Asigna el enlace al array
            lista_articulos.append(contenedor.a.get('href'))
            
    return lista_articulos
```

```python
# Web Scrapper - IMDB Top 250 movies
import requests as rq
from bs4 import BeautifulSoup

# Saving the URL
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Creating the request
page = rq.get(url)

# Making sure the web got the solicitude
page.status_code
print('The status of the request is: {}'.format(page.status_code))

# Creating the soup
soup = BeautifulSoup(page.text, 'lxml')

# Looks like the 'lister' tag has all the information we need
general = soup.find('div', attrs = {'class':'lister'})

# Now let's go deeper
general = soup.find('tbody', attrs= {'class':'lister-list'}).find_all('tr')

# All the information are in these tags, we just need to extract them!
# First, let's create a list with all the links

def link_creation(general):
    section = general[0]
    link_sections = [section.a.get('href') for section in general]
    index = 1
    common = '?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=MBY5AS7XQMWKBXS6Y8N7&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_'
    links = []
    for i in link_sections:
        link = ('www.imdb.com' + str(i) + common + str(index))
        links.append(link)
        index += 1
    
    return links

# Now let's create a list of movie names!

def movie_names(general):
    section = general[0]
    movie_names = [section.find('td', attrs = {'class':'titleColumn'}).a.get_text() for section in general]
    return movie_names

# And for everything else...

def categorics(general):
    section = general[0]
    ratings = [section.find('span', attrs = {'name':'ir'}).get('data-value') for section in general]
    qualifiers = [section.find('span', attrs = {'name':'nv'}).get('data-value') for section in general]
    year = [section.find('span', attrs = {'class':'secondaryInfo'}).get_text() for section in general]
    protagonist_dir = [section.find('td', attrs = {'class':'titleColumn'}).a.get('title') for section in general]

    return(section, ratings, qualifiers, year, protagonist_dir)
```
</details>
<br>

>💡El texto también se puede extraer como:

```python
seccion.a.text
```

Arroja el mismo tipo de dato str, quizá haya diferencia en tiempo de ejecución.

# 7. Manejo de errores