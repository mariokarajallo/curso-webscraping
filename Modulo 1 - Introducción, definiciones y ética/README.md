# Curso de Web Scraping: Extracción de Datos en la Web

## **Modulo I - Introducción, definiciones y ética**
- [Clase 1 Introducción y definiciones](#1-introducción-y-definiciones)
- [Clase 2 Ética y Legalidad](#2-ética-y-legalidad)
- [Clase 3 Configuración del entorno de trabajo con Jupyter](#3-configuración-del-entorno-de-trabajo-con-jupyter)


# 1. **Introducción y definiciones**

`Web Scraping:` Proceso de extracción de datos almacenados en la web.

Objetivo: Recopilar información almacenada en un servicio web.

Aplicación: Productos, reseñas, noticias para hacer posteriormente un análisis.


`Web Crawling`: Proceso de mapeo e indexación de páginas web para conocer su contenido

Objetivo: Conocer la estructura de la web.

Aplicación: Conocer la estructura de la web con el fin de indexar en motores de búsqueda.


**Herramientas del curso:**

- Python
- Jupyter
- Bibliotecas
    - Requests
    - BeautifulSoup
    - Selenium
    - Scrapy

**Lecturas recomendadas:**
- [Documentacion Requets](https://requests.readthedocs.io/en/latest/)
- [Documentacion Beautifulsoup ](https://www.crummy.com/software/BeautifulSoup/)
- [Documentacion Selenium](https://selenium-python.readthedocs.io/)
- [Documentacion Scrapy](https://scrapy.org/)

# 2. **Ética y Legalidad**

## ¿Es legal?
Debemos hacernos las siguientes preguntas.
>¿Estoy violando alguna reglamentación local?
¿Estoy violando los “Términos y Condiciones” del sitio?
¿Estoy accediendo a lugares no autorizados?
¿Es legal el uso que le voy a dar a los datos?
> 

Tenemos estos articulos que hablen y responden estas preguntas.

[https://www.forbes.com/sites/emmawoollacott/2019/09/10/linkedin-data-scraping-ruled-legal/#66d703ba1b54](https://www.forbes.com/sites/emmawoollacott/2019/09/10/linkedin-data-scraping-ruled-legal/#66d703ba1b54)

[https://nubela.co/blog/is-linkedin-scraping-legal/](https://nubela.co/blog/is-linkedin-scraping-legal/)


---

`Robots.txt` En este archivo encontramos información sobre el sitio y nos muestra que  sitios o rutas el dueño de la página no quiere que accedamos. 

Casi todas las paginas tienen un archivo robots.txt para darnos  las buenas practicas de obtención de esas paginas, pero no es  vinculante y no hay nada que no nos permita escrapear todo el sitio. Solo se responsable.

`Disallow:` Rutas que no quieren que se le haga scraping o que sean indexadas. 

`Crawl-delay`: Es el tiempo que debemos configuración entre solicitud al sitio. Para no sobrecargar este sitio.

💡 Importante tener en cuenta este valor:

```
crawl-delay: 30
```
expresado en segundos, y usado en la colección de parámetros a la hora de hacer de sistematizar consultas (scraping) a un sitio web respetando la integridad de respuesta del servidor objetivo

# **3. Configuración del entorno de trabajo con Jupyter**

## Anaconda/Miniconda

La Distribución Anaconda es un paquete de software que cuenta con todo lo necesario para empezar a trabajar en Data Science utilizando Python (o R). Incluye la instalación del intérprete de Python con los  módulos externos más usados en Data Science y diversos entornos de desarrollo entre los que se encuentra Jupyter, el que usaremos durante el curso.

También cuenta con un administrador de paquetes y entornos llamado conda, que nos permitirá crear entornos de trabajo aislados y descargar e  instalar librerías de código externas que iremos viendo durante el curso.

Otra de las ventajas de Anaconda es que es multi-plataforma y cuenta con instaladores para Windows, MacOs y Linux. En este documento te enseñaré a instalar Anaconda en Windows.

Para más información sobre el proceso de instalación de Anaconda e instructivos sobre cómo instalarlo en otros sistemas operativos, te recomiendo que visites la página oficial: [https://docs.anaconda.com/anaconda/install/](https://docs.anaconda.com/anaconda/install/).

## Instalación

A continuación te detallo los pasos para que puedas instalar Anaconda en tu PC con Windows:

1. Navegar al sitio oficial de descargas de Anaconda, [https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)
2. Seleccionar el sistema operativo para acceder a las opciones de descarga.
3. Descargar la versión correspondiente a tu sistema operativo (32 o 64 bits) de Python 3.7.
4. Ejecutar el instalador descargado y no modificar las opciones por defecto. Esto hará que no se generen conflictos con otras instalaciones de Python que puedas tener en tu PC.
5. Elegir el directorio de instalación.
6. No agregar Anaconda a la variable de entorno PATH, a menos que sepas lo que estás haciendo
7. Si quieres puedes instalar PyCharm, que lo usaremos brevemente en el curso, pero la mayor parte de las clases trabajaremos en otro entorno.
8. Una vez instalado, verás esta pantalla con las opciones para acceder a algunos recursos oficiales y la documentación de Anaconda.
9. ¡Listo! Una vez completada la instalación, podrás acceder al Anaconda Navigator y al Jupyter Notebook, el entorno de trabajo que usaremos en el curso.
10. Tambien puedes probar la version de menos peso llamada **Miniconda**.


## Jupyter Notebook desde Visual Studio Code

Gestiona los proyectos dentro de una variable de entorno`venv` incluido el servidor de Jupyter Notebook.

<aside>
💡 "Como parte de las buenas prácticas, antes de seguir crear un entorno virtual para evitar conflictos con dependencias instaladas anteriormente en nuestro computador"

</aside>

Visual Code : [https://code.visualstudio.com/docs/python/data-science-tutorial](https://code.visualstudio.com/docs/python/data-science-tutorial)

Instalaremos el plugins de Jupyter Noteboks, en el apartado de Extensiones


### Crear entorno virtual (Anaconda/Miniconda/VScode)

1. Crear una carpeta con el nombre del proyecto por ejemplo: mkdir webscraping_platzi
2. ingresa a la carpeta del proyecto y crea un entorno virtual:
    1. Inicialmente dentro de una carpeta vacia para el curso creo un entorno virtual para evitar conflictos con dependencias instaladas anteriormente  en mi computador:  desde la terminal ejecutamos`python3 -m venv nombre-entorno-virtual`
3. Una vez instalado y creado nuestro entorno virtual, procedemos a activar : 
    1. Linux → `source nombre-entorno-virtual/bin/activate`
    2. windows →  `**source** nombre-entorno-virtual/Scripts/activate)` 
4. Después de tener el entorno activo instalamos Jupyter:
    1. `python3 -m pip install jupyter`
    2. (no hace falta instalar toda la suite Anaconda) 
5. Instalamos las dos librerías solicitadas en las clases
    1. Instalar requests: `pip install requests`
    2. Instalar Beautiful Soup: `pip install beautifulsoup4`
6. Finalmente si quieren ver las librerías instaladas en su entorno pueden ejecutar el comando:
    1. Verificar que todo se instalo utilizando el comando `pip freeze`


# Crear ambiente virtual con virtualenv

**Ambiente virtual**

Nos permite encapsular un proyecto para poder instalar las versiones de los paquetes que se requieran sin tenerlos que instalar en todo el sistema operativo. Esto evita conflictos de paquetes en el intérprete principal.

**Instalar ambiente virtual**

1. Lo primero que se debe hacer es instalar el paquete de **virtualenv** (*pip install virtualenv*) el cual es el que nos va a permitir crear los entornos virtuales, este se instalará de forma global. Para verificar que se instaló correctamente podemos ejecutar **which virtualenv**.
2. Una vez instalado el **virtualenv** debemos crear o seleccionar la carpeta en donde tendremos nuestro entorno virtual, estando ahí ejecutamos el siguiente para crear el entorno virtual:
**virtualenv name_env ** por convención es recomendable llamarlo *venv*.
3. Después de crear el entorno virtual debemos activarlo, para ello se ejecuta el siguiente comando: **source /venv/Scripts/activate** para *windows*, en *linux* sería **source /venv/bin/activate** con esto quedará activado y nos aparecerá el nombre del entorno virtual al inicio de la línea en la terminal de comandos, (venv en este caso). Para desactivarlo sería lo mismo pero al final se coloca **desactivate**.
4. Para ver los paquetes que tenemos instalados en nuestro entorno virtual ejecutamos el siguiente comando: **pip freeze**. Esto nos mostrará el listado de los paquetes, si no aparece nada es porque no se ha instalado ningún paquete aún.
5. Si queremos tener todos los paquetes agrupados y con su versión correspondiente, podemos hacer uso del archivo *requirements.txt* en donde colocaremos cada uno de los paquetes y que luego podremos instalar usando el siguiente comando: **pip install -r requirements.txt**
6. Para desactivar → deactivate


## **Lecturas Recomendadas**

- Un tutorial básico y sencillo de entender para Jupyter: [https://www.adictosaltrabajo.com/2018/01/18/primeros-pasos-con-jupyter-notebook/](https://www.adictosaltrabajo.com/2018/01/18/primeros-pasos-con-jupyter-notebook/)
- Tambien se pueden usar Google Colab para las notebooks: [https://colab.research.google.com/](https://colab.research.google.com/)