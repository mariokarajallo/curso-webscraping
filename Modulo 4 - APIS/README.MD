# Curso de Web Scraping: Extracción de Datos en la Web

# **Modulo IV - APIS**
- [Clase 20 Introducción a APIs](#20-introducción-a-apis)



# 20. **Introducción a APIs** 

<img src="./img/m4c0-1.png"/>

En este módulo utilizaremos APIs para obtener información sobre artistas, discos y tracks disponibles en Spotify.

¿Qué es una **API**?

Por sus siglas en inglés, una API es una interfaz para programar aplicaciones (*Application Programming Interface*).
Es decir que es un conjunto de funciones, métodos, reglas y definiciones que nos permitirán desarrollar aplicaciones (en este caso un scraper) que se comuniquen con los servidores de Spotify. Las APIs son diseñadas y desarrolladas por las empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que utilicen sus servicios. Spotify tiene APIs públicas y bien documentadas que estaremos usando en el desarrollo de este proyecto.

### REST
Un término que seguramente te vas a encontrar cuando estés buscando información en internet es **REST** o *RESTful*. Significa *representational state transfer* y si una API es REST o RESTful, implica que respeta unos determinados principios de arquitectura, como por ejemplo un protocolo de comunicación cliente/servidor (que será HTTP) y (entre otras cosas) un conjunto de operaciones definidas que conocemos como **métodos**. Ya veníamos usando el método GET para hacer solicitudes a servidores web.

### Documentación
Como mencioné antes, las APIs son diseñadas por las mismas empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que consuman sus servicios o información. Es por eso que la forma de utilizar las APIs variará dependiendo del servicio que queramos consumir. No es lo mismo utilizar las APIs de Spotify que las APIs de Twitter. Por esta razón es de suma importancia leer la documentación disponible, generalmente en la sección de desarrolladores de cada sitio. Te dejo el [link a la de Spotify](https://developer.spotify.com/documentation/)

### JSON
Json significa *JavaScript Object Notation* y es un formato para describir objetos que ganó tanta popularidad en su uso que ahora se lo considera independiente del lenguaje. De hecho, lo utilizaremos en este proyecto por más que estemos trabajando en Python, porque es la forma en la que obtendremos las respuestas a las solicitudes que realicemos utilizando las APIs. Para nosotros, no será ni más ni menos que un diccionario con algunas particularidades que iremos viendo a lo 
largo del curso.

Hay muy buenas APIs gratuitas en la web para practicar Machine Learning, aquí hay una lista: [https://todobi.com/las-mejores-apis-para-machine-learning/](https://todobi.com/las-mejores-apis-para-machine-learning/)

# 21. **Utilizando APIs: Construir una URL** 

> #### [M4C1 Construir una URL](M4C1-construir-url.ipynb) puedes mirar este archivo como guía de esta sección.

Links útiles para la clase:
- Documentación de Spotify - Web API Reference - Artistas

[Web API Reference | Spotify for Developers](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist)

- Coldplay en Spotify, aqui podemos ver el id del artista.

[Coldplay](https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU)

## Empecemos!

```python
#Importamos la libreria que utilizaremos para consumir y hacer peticiones
import requests
```

```python
#URL base para peticiones GET de la api de SPOTIFY
url_base='https://api.spotify.com/v1'
```

```python
#guardamos el id de la pagina del artista de spotify en este ejemplo el id de coldplay
id_artist='4gzpq5DPGxSnKTe4SA8HAU'
```

```python
#ruta de ENDPOINT para artistas (ver documentacion API)
ep_artist='/artists/{id}'
```

```python
#unificamos nuestra URL final
url_base+ep_artist.format(id=id_artist)
```

```python
#creamos nuestra peticion con la libreria requests
# y pasamos como parametro la URL que construimos de la api de SPOTIFY
r=requests.get(url_base+ep_artist.format(id=id_artist))
```

'https://api.spotify.com/v1/artists/4gzpq5DPGxSnKTe4SA8HAU'

```python
#vemos el estado que nos desvuelve la peticion
r.status_code
```

401

```python
# status code = 401 ; significa que no estamos autorizados a acceder al ENDPOINT
#utilizamos este metodo para visualizar lo que devuelve el JSON de nuestro peticion
r.json()
```

{'error': {'status': 401, 'message': 'No token provided'}}

> 🛠 Por el momento es todo, continuaremos en la siguiente sección.

# 22. **Utilizando APIs: Tokens y Búsqueda** 

> #### [M4C2 Tokens y Búsqueda](M4C2-tokens-y-busqueda.ipynb) puedes mirar este archivo como guía de esta sección.