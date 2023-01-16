# Curso de Web Scraping: Extracción de Datos en la Web

# **Modulo IV - APIS**
- [Clase 20 Introducción a APIs](#20-introducción-a-apis)
- [Clase 21 Utilizando APIs: Construir una URL](#21-utilizando-apis-construir-una-url)
- [Clase 22 Utilizando APIs: Tokens y Búsqueda](#22-utilizando-apis-tokens-y-búsqueda)

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

## **Autenticación / autorización**

Primero debemos crear un Client ID que es el que usaremos para acceder a la información a través de las APIs de Spotify. 

- https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app
    
    Spotify te requiere registrar tu aplicación para poder utilizar la api, sigue la documentación para ello.
    
    Regístrate [https://developer.spotify.com/dashboard/tos-accept](https://developer.spotify.com/dashboard/tos-accept)
    
    Y luego creamos un una app en el dashboard
    
    <img src="./img/m4c2-1.png"/>
    
    una vez registrada nuestra aplicación nos genera un `cliente_id`  y un `client_secret.`
    
    El cual nos permitirá poder acceder a un `tokens` , y con este token lo vamos a utilizar en el `header` requerido en los `endpoint`
    
    <img src="./img/m4c2-2.png"/>
    

Existen distintas maneras para generar el Tokens, nosotros utilizaremos la mas sencilla, por que solamente queremos acceder a la información de un artista en particular.

- [https://developer.spotify.com/documentation/general/guides/authorization/use-access-token/](https://developer.spotify.com/documentation/general/guides/authorization/use-access-token/)
- [https://developer.spotify.com/documentation/general/guides/authorization/code-flow/](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)

Para codificar en base 64 

- https://www.base64encode.org/

Endpoint de búsqueda de Spotify

- [https://developer.spotify.com/documentation/web-api/reference/#/operations/search](https://developer.spotify.com/documentation/web-api/reference/#/operations/search)

## EMPECEMOS!

```python
# Importamos la libreria que utilizaremos para consumir y hacer peticiones
import requests
import pandas as pd
```

```python
# URL base para peticiones GET de la api de SPOTIFY
url_base='https://api.spotify.com/v1'
```

```python
# guardamos el id de la pagina del artista de spotify en este ejemplo el id de coldplay
# este ID lo buscamos manualmente entrando en la pagina de spotify del artista
id_artist='4gzpq5DPGxSnKTe4SA8HAU'
```

```python
# ruta de ENDPOINT para artistas
# Los endpoints son las URLs de un API o un backend que responden a una petición.
ep_artist='/artists/{id}'
```

```python
#unificamos nuestra URL final y le damos formato al endpoint del artista
# de esta manera asignamos nuestro ID de coldplay al endpoint
url_artist=url_base+ep_artist.format(id=id_artist)
```

```python
#creamos nuestra peticion con la libreria requests
# y pasamos como parametro la URL de la api de SPOTIFY para obtener informacion respecto con el ID del artista
r_spotify=requests.get(url_artist)
```

'https://api.spotify.com/v1/artists/4gzpq5DPGxSnKTe4SA8HAU'

```python
#vemos el estado que nos desvuelte la peticion
r_spotify.status_code
```

401

```python
#utilizamos este metodo para visualizar lo que devuelve el JSON de nuestro peticion
r_spotify.json()
```

{'error': {'status': 401, 'message': 'No token provided'}}

### Como no poseemos las credenciales de acceso o token, seguiremos un flujo  para obtener las credenciales de acceso a la api

[https://developer.spotify.com/documentation/general/guides/authorization/code-flow/](https://developer.spotify.com/documentation/general/guides/authorization/code-flow/)

<img src="./img/m4c2-3.png"/>

```python
# desde esta URL obtendremos acceso a un token valido para el acceso a la api
token_url='https://accounts.spotify.com/api/token'
```

```python
# creamos los parametros para obtener un token de acceso a la api
# estos parametro debemos pasarle al requests en el momento que ejecutemos el la peticion GET
params={'grant_type':'client_credentials'}
```

como accedemos al token ? Flujo de credenciales/tokens de cliente:

<img src="./img/m4c2-4.png"/>

<img src="./img/m4c2-5.png"/>

para el valor de de `Authorization` debemos de pasar nuestro `Client ID` y `Client Secret` codificados en base64, estos estring lo obtuvimos al crear la aplicación.

<img src="./img/m4c2-6.png"/>

<img src="./img/m4c2-7.png"/>

ingresamos a la interfaz  `[https://www.base64encode.org/](https://www.base64encode.org/)` para codificar nuestros propios strings en este caso `Client ID` y `Client Secret` debemos pasar al formato base64

<img src="./img/m4c2-8.png"/>

de esta manera obtenemos los valores de nuestros string codificados para nuestra cabecera

`Authorization: Basic <base64 encoded client_id:client_secret>` y obtener el token

```python
# aparte de los parametros, vamos a tener que pasarle un encabezado
# es otro diccionario donde devolvemos nuestro client_id y client_secreta codificado en base64
headers={'Authorization':'Basic MDI5NTI4OTQzNWMyNDc2Yjk2YWVhYTYzNTk1ODQzZjQ6NTBlYzcwMmY1YjkxNDIxMDhmNzNiNzE1MjA4NGNjNWM='}
```

```python
#ahora si podemos solicitar el token, haciendo una request con el metodo POST
# a nuestro token URL le pasamos los datos que son los parametros y un encabezado
r_token = requests.post(token_url, data=params, headers=headers )
```

```python
# una vez generado la solicitud, vemos el estado 
r_toke.status_code
```

200

```python
# vemos el json con los datos generados para el acceso a la API
r_token.json()
# si obtuvimos una respuesta correcta, veremos el access token, el tipo de token y el vencimiento del token
```

{'access_token': 'BQBWWXdPOgXzdsbrsLex6Vaha',
'token_type': 'Bearer',
'expires_in': 3600}

```python
# un JSON no es mas ni menos que un diccionario, guardamos el valor del access_token en una variable, para acceder al token directamente
token = r_token.json()['access_token']
```

Cómo usar el token de acceso, debemos crear nuevamente nuestra cabecera o encabezado e indicarle que tipo de token obtuvimos

[https://developer.spotify.com/documentation/general/guides/authorization/use-access-token/](https://developer.spotify.com/documentation/general/guides/authorization/use-access-token/)

entonces nuestro `header` se compone de un diccionario: llave → `Authorization` valor→`Bearer <Access Token>`

<img src="./img/m4c2-9.png"/>

```python
# formatemoa el valor de Bearer con el token que obtuvimos
header = {"Authorization":"Bearer {}".format(token)}
```

una vez que tenemos el encabezado listo, ahora podemos acceder a la api

```python
# hacemos una peticion a la api de spotify para obtener los datos de nuestro artista 
# y como estamos autorizados pasamos el encabezado a nuestra peticion
r_spotify= requests.get(url_artist, headers=header)
```

```python
# Aqui verificamos que nos devuelva una respuesta optima
r_spotify.status_code
#//200
```

```python
# ahora si obtuvimos un diccionario con toda la informacion de nuestro artista que tiene spotify
# para visualizar nuestro diccionario de datos de tipo json
r_spotify.json()
```

{'external_urls': {'spotify': 'https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU'}, 

'followers': {'href': None, 'total': 39856733},
 'genres': ['permanent wave', 'pop'],
 'href': 'https://api.spotify.com/v1/artists/4gzpq5DPGxSnKTe4SA8HAU',
 'id': '4gzpq5DPGxSnKTe4SA8HAU', 'images': [{'height': 640, 'url': ' [https://i.scdn.co/image/ab6761610000e5eb989ed05e1f0570cc4726c2d3](https://i.scdn.co/image/ab6761610000e5eb989ed05e1f0570cc4726c2d3)',   'width': 640},  {'height': 320,   'url': 'https://i.scdn.co/image/ab67616100005174989ed05e1f0570cc4726c2d3',   'width': 320},  {'height': 160,   'url': 'https://i.scdn.co/image/ab6761610000f178989ed05e1f0570cc4726c2d3',   'width': 160}], 'name': 'Coldplay', 'popularity': 88, 'type': 'artist', 'uri': 'spotify:artist:4gzpq5DPGxSnKTe4SA8HAU'}

### Ahora podremos hacer uso del ENDPOINT para hacer búsquedas

[https://developer.spotify.com/documentation/web-api/reference/#/operations/search](https://developer.spotify.com/documentation/web-api/reference/#/operations/search)

<img src="./img/m4c2-10.png"/>

Podremos buscar el ID de un artista, sin la necesidad de tener que cargar manualmente, a continuación vamos a generar una URL de búsqueda

 

```python
#direccion del ENDPOINT para realizar busquedas
url_busqueda='https://api.spotify.com/v1/search'
```

si revisamos la documentación vemos que este ENDPOINT nos pide algunos parámetros requeridos

<img src="./img/m4c2-11.png"/>

```python

# creamos los parametros para la busqueda
# un diccionario que contenga la Query q->string , type->array
search_params={'q': 'coldplay', 'type':'artist'}
```

```python
# hacemos la solicitud tipo GET donde consumiremos lo que buscamos pasando los siguientes parametros
# Url de busqueda (ENDPOINT), Header (autenticacion), params (parametros de busqueda)
r_busqueda=requests.get(url_busqueda,headers=header,params=search_params)
```

```python
# si todo salio bien debemos de esperar una respuesta optima
r_busqueda.status_code
#// 200
```

```python
# vemos todo lo que nos trajo el resultado de la busqueda en el json
r_busqueda.json()
# un diccionario bastante cargado de informacion, con varias bandas que tienen el nombre de nuestro artista
```

En la respuesta de nuestra búsqueda tenemos en nuestro diccionario json todos los artistas con el nombre `coldplay`, y en la llave `items` los valores sobre cada resultado de nuestros artistas con el nombre coldplay.

```python
# visualizamos nuestro json con las llave que nos interesan
# entonces dentro de nuestra llave artist, nos quedamos con los valores de items, que son nuestros resultados de busqueda
df = pd.DataFrame(r_busqueda.json()['artists']['items'])
df.head()
```

para obtener exactamente nuestro artista “buscado”, la banda original de coldplay, sabemos que sera el artista con mayor popularidad dentro de spotify entre todos los artistas que poseen el nombre “coldplay” , es por eso que vamos a filtrar nuestro data frame teniendo en cuenta el siguiente criterio.

1. Ordenamos el df por popularidad
2. quedarse con la primera fila
3. quedarse con la columna id

```python
# ordenamos en base a la columna popularity de myor a menor
# me quiero quedar con el primer elemento de este data frame
# iloc[0] tenemos el primer elemento y si quiero sola la columna id colocamos el nombre de la columna['id']
df.sort_values(by='popularity', ascending=False).iloc[0]['id']
```

'4gzpq5DPGxSnKTe4SA8HAU’

de esta manera obtuvimos el Id de nuestro artista coldplay, pero esta vez gracias al uso de la api y no manualmente como lo hicimos en el principio del ejercicio cuando buscamos el id del artista en la pagina de spotify del artista.

---

### Otros ejercicios resueltos:

### Ejercicio 1

```python
import requests, base64, pandas

URL_SPOTYFY = 'https://api.spotify.com/v1'
EP_ARTIST = '/artists/{artist_id}'
URL_SPOTYFY_SRCH = 'https://api.spotify.com/v1/search'
TOKEN = 'https://accounts.spotify.com/api/token'

def encoding():
    clien_id = "xxxxxxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxx"
    msg_bytes = clien_id.encode("UTF-8")
    msg_base64 = base64.b64encode(msg_bytes)
    msg_decode = msg_base64.decode("UTF-8")
    return msg_decode
        

def token_spotify():
    try:  
        params = {'grant_type': 'client_credentials'}
        headers = {'Authorization': 'Basic ' + encoding()}
        r_spoty = requests.post(TOKEN, headers=headers, data=params)

        return r_spoty.json()["access_token"]
    except Exception as erre:
        print(f"Error al requerir el token:  \n {erre}")

def api_spotify(inp):
    try:
        # url = URL_SPOTYFY + EP_ARTIST.format(artist_id=AVICII)
        header = {'Authorization': 'Bearer {}'.format(token_spotify())}
        srch_params = {'q' : inp, 'type' : 'artist', 'market' : 'CO'}
        get_url = requests.get(URL_SPOTYFY_SRCH, headers=header, params=srch_params)
        df = pandas.DataFrame(get_url.json() ['artists'])
        # print(get_url.json())
        print(df.head)
    except Exception as erre:
        print(f"Error en la api:  \n {erre}")

if __name__ == "__main__":
    inp = input(f"Que artista desaea buscar?: ")
    api_spotify(inp)
```

### Ejercicio 2

el método que construí utilizando la librería la autenticación OAuth 2.0 disponible para la librería request. Con este paso, lo que me evito es que tener que codificar manualmente el token base 64.

```python
# instalar librerías
!pip3 install requests requests.auth

#importarlas librerías al notebook
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
from requests_oauthlib import OAuth2Session

# declarar variables de la API de Spotify
client_id  = 'a1f9ce...663d3'
client_secret = 'e6425...62800'

# variable para la autenticación
auth = HTTPBasicAuth(client_id, client_secret)
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# pedir el token a la API de Spotify
token = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=auth)
# validar la obtención del token
token

####### abrir otro bloque de código #######

# definir el endpoint de busqueda (search). A esta url le mandaremos la petición
url_search = 'https://api.spotify.com/v1/search'

# variables de la petición. Vamos a descubrir cuáles son los artistas que se llaman "Marc"
headers = {'Accept': 'application/json',
           'Content-Type' : 'application/json',
           'Authorization' : 'Bearer '+ token['access_token']}
payload = {'q' : 'Marc',
           'type' : 'artist',
           'market' : 'US',
           'limit' : '10'}

# petición utilizando la librería request.
response_search = requests.get(url_search,params=payload,headers=headers)
# ver resultado
response_search.json
```