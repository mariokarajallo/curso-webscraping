# Curso de Web Scraping: Extracción de Datos en la Web

# **Modulo IV - APIS**
- [Clase 20 Introducción a APIs](#20-introducción-a-apis)
- [Clase 21 Utilizando APIs: Construir una URL](#21-utilizando-apis-construir-una-url)
- [Clase 22 Utilizando APIs: Tokens y Búsqueda](#22-utilizando-apis-tokens-y-búsqueda)
- [Clase 23 Utilizando APIs: Obteniendo la discografía](#22-utilizando-apis-obteniendo-la-discografía)

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

# 23. **Utilizando APIs: Obteniendo la discografía** 

> #### [M4C3 Obteniendo la discografía](M4C3-obteniendo-discografia.ipynb) puedes mirar este archivo como guía de esta sección.


Ya conseguimos el ID de nuestro artista, ahora utilizaremos ese ID para conseguir toda la discografía.

Con el tiempo necesitaremos reutilizar el token de acceso a la api de spotify, (los token proveídos por spotify tienen un limite de tiempo, se vencen) así que necesitamos actualizar nuestros tokens.

Empezamos utilizando una nueva librería `base64` que permite codificar nuestro `cliente_id` y `client_secret` provisto por la aplicación que creamos en el dashboard de spotify, de esta manera no necesitaremos codificar en base64 manualmente en una interfaz externa, y podremos crear una función en nuestro código para generar un token valido cada vez que necesitemos.

## Empecemos!

### código sección anterior

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

```python
#vemos el estado que nos desvuelte la peticion
r_spotify.status_code
```

```python
#utilizamos este metodo para visualizar lo que devuelve el JSON de nuestro peticion
r_spotify.json()
```

```python
# desde esta URL obtendremos acceso a un token valido para el acceso a la api
token_url='https://accounts.spotify.com/api/token'
```

```python
# creamos los parametros para obtener un token de acceso a la api
# estos parametro debemos pasarle al requests en el momento que ejecutemos el la peticion GET
params={'grant_type':'client_credentials'}
```

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

```python
# vemos el json con los datos generados para el acceso a la API
r_token.json()
# si obtuvimos una respuesta correcta, veremos el access token, el tipo de token y el vencimiento del token
```

```python
# un JSON no es mas ni menos que un diccionario, guardamos el valor del access_token en una variable, para acceder al token directamente
token = r_token.json()['access_token']
```

```python
# formatemoa el valor de Bearer con el token que obtuvimos
header = {"Authorization":"Bearer {}".format(token)}
```

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

```python
#direccion del ENDPOINT para realizar busquedas
url_busqueda='https://api.spotify.com/v1/search'
```

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

```python
# visualizamos nuestro json con las llave que nos interesan
# entonces dentro de nuestra llave artist, nos quedamos con los valores de items, que son nuestros resultados de busqueda
df = pd.DataFrame(r_busqueda.json()['artists']['items'])
df.head()
```

```python
# ordenamos en base a la columna popularity de myor a menor
# me quiero quedar con el primer elemento de este data frame
# iloc[0] tenemos el primer elemento y si quiero sola la columna id colocamos el nombre de la columna['id']
df.sort_values(by='popularity', ascending=False).iloc[0]['id']
```

### codigo nuevo
como los tokens se vencen, sera de utilidad tener una función que nos permita renovar el token periódicamente, para ellos haremos uso de la librería base64, que nos permitirá codificar el `client_id` y `client_secret` para poder acceder a la api de autorización de spotify

```python
import base64
```

```python
def get_token(client_id, client_secret):
		#codificamos el client_id y client_secret
    encoded = base64.b64encode(bytes(client_id+':'+client_secret, 'utf-8'))
		# para la nueva solicitud, creamos los parametros
    params = {'grant_type':'client_credentials'}
		# creamos el encabezado, donde concatemos el string codificado
    header={'Authorization': 'Basic ' + str(encoded, 'utf-8')}
		# hacemos la solicitud tipo POST a la URL de autenticacion
    r_token= requests.post('https://accounts.spotify.com/api/token', headers=header, data=params)
    if r_token.status_code != 200:
				# si el resultado (status code) no es 200 significa que hubo problemas
				# mostramos la respuesta que nos da
        print('Error en la request.', r_token.json())
				#y no devolvemos nada
        return None
		# caso contrario devolvemos un print y retornamos la respuesta pero solamente el acces_token
    print('Token válido por {} segundos.'.format(r_token.json()['expires_in']))
    return r_token.json()['access_token']
```

```python
# del dashboard de nuestra aplicacion de spotify guardamos nuestro client_id y client_secret
client_id='0295289435c2476b96aeaa63595843f4'
client_secret= '50ec702f5b9142108f73b7152084cc5c'
# utilzamos la funcion get_token, pasando el client_id, client_secret
token=get_token(client_id, client_secret)
```

con el token nuevo generado, utilizaremos para armar un nuevo header

```python
header={'Authorization':'Bearer {}'.format(token)}
```

ahora cada vez que tengamos hacer un nuevo proceso de scraping o de utilización de la api, solo deberemos de llamar a la función get_token para obtener un token nuevo, que vamos a saber que es valido.

```python
# vemos nuestro id de artista nuevamente
id_artist
```

ahora lo que podemos hacer es obtener los álbumes de nuestro artista para eso vemos en la documentación  cuales son los endpoint del Álbum del artista

<img src="./img/m4c3-1.png"/>

```python
# guardamos la ruta del ENDPOINT
ep_album_artist='/artists/{id}/albums'
```

```python
#recordemos que tenemos nuestra URL base
url_base
```

https://api.spotify.com/v1

```python
#para armar la url completa de de busqueda de albun de artista
url_album_artist= url_base+ep_album_artist.format(id=id_artist)
```

https://api.spotify.com/v1/artists/`4gzpq5DPGxSnKTe4SA8HAU`/albums

ahora creamos los parámetros que necesitamos que nos devuelva esta URL del álbum de artista

<img src="./img/m4c3-2.png"/>

```python
# utilizando el parametro market podemos indicarle los albumes que queremos de un determinado pais
params={'market':'PY', 'include_groups':'album'}
```

```python
# generamos una nueva resquets pasando la URL de donde queremos consumir, la cabecera que indica la autorizacion y los parametros que queremos obtener
albums_artist= requests.get(url_album_artist, headers=header, params=params)
```

```python
#vemos la respuesta de nuestro solicitud
albums_artist.status_code
```

200

```python
# revisamos el JSON, y en la llave de items, tenemos una lista que contiene todos los albumes de nuestra artista
album_artist.json()['items']
```

En cada items, podemos ver que tenemos la cantidad de traks, nombre del álbum, el id de cada uno de los álbumes, portada etc.

Recorremos el array de la llave `items`  de nuestro json, para obtener los valores de cada álbum

```python
lista_albums = [(album['id'], album['name'],album['release_date']) for album in album_artist.json()['items']]
lsita_albums
```

[('06mXfvDsRZNfnsGZvX2zpb', 'Music Of The Spheres', '2021-10-15'),
('2FeyIYDDAQqcOJKOKhvHdr', 'Everyday Life', '2019-11-22'),
('4dBp8rzdqH9unSndGk6g6o', 'Everyday Life', '2019-11-22'),
('19CvkGjYpifkdwgVJSbog2', 'Live in Buenos Aires', '2018-12-07'),
('3cfAM8b8KqJRoIzt3zLKqw', 'A Head Full of Dreams', '2015-12-04'),
('1hNS0RsxPTFjmKXCgmjSLS', 'Ghost Stories Live 2014', '2014-11-21'),
('2G4AUqfwxcV1UdQjm2ouYr', 'Ghost Stories', '2014-05-19'),
('2OkEsqGTfu8PWRrNHzfr0m', 'Live 2012', '2012-11-19'),
('2R7iJz5uaHjLEVnMkloO18', 'Mylo Xyloto', '2011-10-24'),
('3pboBm7GTa6V5dFXXCt52b', 'LeftRightLeftRightLeft (Live)', '2009-05-15'),
('71pRFAwHBLrjKYRG7V1Q2o', "Viva La Vida (Prospekt's March Edition)",'2008-11-24'),
('1CEODgTmTwLyabvwd7HBty','Viva La Vida or Death and All His Friends','2008-05-26'),
('4E7bV0pzG0LciBSWTszra6', 'X&Y', '2005-06-07'),('3JMOZD2qixTTLRW9I6JuF4', 'Live 2003', '2003-1-01'),
('0RHX9XECH8IVI3LNgWDpmQ', 'A Rush of Blood to the Head', '2002-08-08'),('6ZG5lRT77aJ3btmArcykra', 'Parachutes', '2000-07-10'),
('574iaZA34RiT9rM1F2s2IM', 'Biutyful', '2022-07-06'),
('7lbSZjlBsWuXtR3WqsdOSN', 'Let Somebody Go (Ofenbach Remix)', '2022-04-15'),
('1mbwiDXEr8l6mK7o76dqyu', 'Let Somebody Go (Piano Version)', '2022-03-18'),
('7EZAIhKzfjXbAsL0hrQjGF', 'Let Somebody Go (Kygo Remix)', '2022-03-11')]

Ahora que obtuvimos el id de cada álbum de nuestro artista podemos obtener los elementos o datos de cada álbum o un álbum en particular gracias a su id.

<img src="./img/m4c3-3.png"/>

```python
#seleccionamos el id de un album en aprticular
id_album_artist='06mXfvDsRZNfnsGZvX2zpb'
```

```python
# creamos la ENDPOINT para el album
ep_album='/albums/{id}'.format(id=id_album_artist)
```

```python
# creamos la ruta completa del ENDPOINT
url_album_artist=url_base+ep_album
url_album_artist
```

'https://api.spotify.com/v1/albums/06mXfvDsRZNfnsGZvX2zpb’

```python
# creamos el parametro para el endpoint de album de la api
# en market indicamos el pais donde esta disponible el contenido del album
# en include_groups se especifica el tipo de album.
album_params={'market':'PY', 'include_groups':'album'}
```

```python
#hacemos la peticion GET pasando la URL del endpoint, la cabecera con su autorizacion, y los parametros de la peticion
r_album_artist= requests.get(url_album_artist, headers=header, params=album_params)
# seleccionamos de nuestro album el elementro tracks, que contiene una lista de items, que son las musicas con su nombre, id etc de cada musica.
r_album_artist.json()['tracks']['items']
```

```python
#ahora si podemos obtener el id y el name de cada track, recorriendo la lista items de tracks
info_album=[(track['id'], track['name']) for track in r_album_artist.json()['tracks']['items']]
info_album
```

[('1a3G9SNslcKsPAOuIikaxd', '🪐'),
('65OR4ywy8Cgs3FDHK82Idl', 'Higher Power'),
('23BO6YozrAXUta1buxFZ80', 'Humankind'),
('1danObd53GynoY83wRz3Ua', '✨'),
('4cGqn0E8JCSY9gQllQj4Mf', 'Let Somebody Go'),
('3oTYv0yShT4sjuPncoUXfK', '❤️'),
('5ophZLHA9mwSZhQSmboyDN', 'People of The Pride'),
('2L2mM3rEO3arNIMQnb3dou', 'Biutyful'),
('0RbekAlUrwR6ZWJdwB3V4y', '🌎'),
('46HNZY1i7O6jwTA7Slo2PI', 'My Universe'),
('2wleRXcIPqltoDPLMH5WDa', '♾'),
('0jH7gF7KCk2Lom9gimaKms', 'Coloratura')]

---

## Otros Ejercicios Resueltos

> 🛠 Obtener el id y nombre de cada álbum de nuestro artista

#### Ejercicio1

Para obtener el id y nombre de cada álbum

```python
# obtener información de cada album de un artista
for album in album_list:
    album_id = album['id']
    album_name = album['name']
    album_dict = {'id': album_id, 'nombre': album_name}
    print(album_dict)

```

#### Ejercicio2

```python
def get_albums_per_artist(artist_id, token, **kwargs):
    rkwargs = {'url': base_url + ep_albums.format(artist_id=artist_id)}
    if not kwargs:
        rkwargs['headers'] = {'Authorization': 'Bearer {}'.format(token)}
        rkwargs['params'] = {'Country': 'PE'}
    r = requests.get(**rkwargs, **kwargs)
    if r.status_code != 200:
        print('Error en la request', r.json())
        return None
    return r.json()['items']
```

#### Ejercicio3

```python
def get_album_info():
    token = get_token(cliente_id,cliente_secret)
    header = {'Authorization':"Bearer " + token}
    ep_albums = url_api_artist + "/albums"
    albums_r = requests.get(ep_albums, headers= header)
    id_albums = [albums_r.json()['items'][i]['id'] for i in range(len((albums_r.json()['items'])))]
    dicter = {}
    counter = 0
    for id_album in id_albums:
        counter += 1
        ep_albums_id = "https://api.spotify.com/v1/albums/" + id_album
        albums_id_r = requests.get(ep_albums_id, headers= header)
        print(albums_id_r.status_code)
        dicter[counter] = albums_id_r.json()['release_date']
    return dicter
get_album_info()
```

#### Ejercicio4

```python
def get_info_album_list(album_list, token):
    url_base = 'https://api.spotify.com/v1'
    ep_album_info = '/albums/{album_id}'
    header = {'Authorization':'Bearer {}'.format(token)}
    params = {'country':'AR'}

    lista = []
    for album in album_list:
        album_info = requests.get(url_base + ep_album_info.format(album_id = album[0]), headers=header, params=params )
        if album_info.status_code == 200:
            added = album_info.json()
            lista.append(added)
        else:
            print(f"HTTP error: {album_info.status_code}")
    return lista
```

#### Ejercicio5

```python
lista_albums = [(album['id'], album['name'], album['release_date'], album['total_tracks']) for album in albums_im.json()['items']]
lista_albums
```

#### Ejercicio6

```python
# Obtención de albums
# Entrega el resultado del request
def get_albums(artist_id):
    url_base = 'https://api.spotify.com/v1/artists/'
    header = {'Authorization': 'Bearer {}'.format(token)}
    # endpoint de los albums
    ep_albums = '{artist_id}/albums'
    url_base + ep_albums
    params = {'country': 'CO'}

    try:
        albums_artist = requests.get(url_base+ep_albums.format(artist_id=id_metallica), headers=header, params=params)
        if albums_artist.status_code == 200:
            return albums_artist
        else:
            print(f'HTTP error: {albums_artist.status_code}')
    except Exception as e:
        print('Error: ', e)
```

**Función para obtener el id de los albums:**

```python
# Entrega una lista con el id de los albums
def get_id_albums(albums_request):
    id_albums = []
    try:
        albums = len(albums_request.json()['items'])
        for album in range(albums):
            id_albums.append(albums_request.json()['items'][album]['id'])
        return id_albums
    except Exception as e:
        print('Error: ', e)
```

**Función para obtener la información de un album:**

```python
def get_info_album(id_album):
    url_base = 'https://api.spotify.com/v1/albums/'
    ep_album = '{album_id}'
    params = {'country': 'CO'}

    # uso de la función para obtener un token válido
    #token = get_token(client_id, client_secret)
    header = {'Authorization': 'Bearer {}'.format(token)}

    try:
        album_artist = requests.get(url_base+ep_album.format(album_id=id_album), headers=header, params=params)
        if album_artist.status_code == 200:
            return album_artist
        else:
            print(f'HTTP error: {album_artist.status_code}')
    except Exception as e:
        print('Error: ', e)
```

#### Ejercicio7

Comparto mi código con la solución al reto.

1. El usuario escribe el artista que quiere scrapear
2. El usuario puede escoger si desea ver una lista con los artistas que su nombre es similar al que escribió, ordenados ascendentemente según
su popularidad
3. El programa muestra los álbumes del artista más popular

```python
import requests
import pandas as pd
import base64

def main(user_artist):
    client_id = 'your Client ID '
    client_secrect = 'your client secrect id'

    artist(get_token(client_id,client_secrect),user_artist)

def get_token(client_id,client_secrect):
    encoded = base64.b64encode(bytes(client_id+':'+client_secrect, 'utf-8'))
    params = {'grant_type':'client_credentials'}
    header = {'Authorization':'Basic '+ str(encoded, 'utf-8')}
    r = requests.post('https://accounts.spotify.com/api/token', headers=header, data=params)
    if r.status_code != 200:
        print('Request error.', r.json())
        return None
    print('Valid token by {} seconds'. format(r.json()['expires_in']))
    token = r.json()['access_token']

    return token

def artist(token,user_artist):
    search_url = 'https://api.spotify.com/v1/search'
    search_params = {'q': user_artist , 'type' : 'artist', 'market' : 'CO'}
    header = {'Authorization' : 'Bearer {}'.format(token)}
    search = requests.get(search_url, headers=header, params=search_params)
    if search.status_code != 200:
        print('Request artist error', search.json())
        return None

    df_artist = pd.DataFrame(search.json()['artists']['items'])
    artist_id = df_artist.iloc[0]['id']

    artists_id = []
    for i in range(len(df_artist['id'])):
        artists_id.append(df_artist.iloc[i]['id'])

    artist_popularity = df_artist.sort_values(by='popularity', ascending=False).loc[0:,'name':'popularity']
    view_artist = input(str('Show all artist?  y/n   '))
    if view_artist == 'y':
        print(artist_popularity)
    else:
        pass

    album(token,artist_id)

def album(token,artist_id):
    header = {"Authorization": "Bearer {}".format(token)}
    url_base = 'https://api.spotify.com/v1'
    ep_albums = '/artists/{artist_nid}/albums'
    params = {'country':'CO'}

    albums = []
    albums_artist = requests.get(url_base + ep_albums.format(artist_nid=artist_id), headers=header, params=params)
    if albums_artist.status_code == 200:
        df_albums = pd.DataFrame(albums_artist.json())
        for i in range(len(df_albums)):
            name = df_albums.loc[i,'items'].get('name')
            albums.append(name)

        print(albums)

    else:
        print(f"Fail in request. HTTP error: {albums_artist.status_code}{albums_artist.json()}")

if __name__ == "__main__":
    print('Welcome to Spotify Scraper')
    user = input(str('Choose an artist to scrape:\n - '))
    user_artist = user.replace(' ','+')
    main(user_artist)```
```

#### Ejercicio8

Tres funciones, la primera para obtener el id de los álbumes

```python
def albums_id(items):
    discografia=[]
    for i in range(len(items)):
        album_id=items[i]['id']
        discografia.append(album_id)
    return discografia
```

La segunda, para obtener el endopoint de los álbumes

```python
def get_endpoint(discos):
    discos=albums_id(items)
    ep_discografia = '/albums/{id}'
    url_discografia =url_base+ep_discografia
    albumes=[]
    for disco in discos:
        header = {'Authorization':'Bearer {}'.format(token)}
        params = {'country': 'CO'}
        d=ep_discografia.format(id=disco)
        discografia_hu = requests.get(url_base+ep_discografia.format(id=disco), headers=header, params=params)
        albumes.append(d)
    return albumes
```

Y finalmente, la tercera función para obtener la discografía

```python
def get_discography(albumes):
    albumes
    discografia = []
    for i in range(len(albumes)):
        disco_params = {'available_markets': 'CO'}
        header = {'Authorization':'Bearer {}'.format(token)}
        url_albumes=url_base+albumes[i]
        albumes_hu = requests.get(url_albumes, headers=header, params=disco_params)
        discography=discografia.append(albumes_hu.json()['name'])
    print(f'Total de albumes al dia de hoy: {len(discografia)}\nTitulo de los albumes: \n{discografia}')
    return discografia
```
