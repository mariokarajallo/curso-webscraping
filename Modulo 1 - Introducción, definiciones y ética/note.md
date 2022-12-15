
- Modulo I - Introducción, definiciones y ética
    - [Clase 1 Introducción y definiciones](#clase-1-introducción-y-definiciones)
    - [Clase 2 Ética y Legalidad](#ética-y-legalidad)
    - [Clase 3 Configuración del entorno de trabajo con Jupyter](#clase-3-configuración-del-entorno-de-trabajo-con-jupyter)




# 1. **Introducción y definiciones**

`Web Scraping:` Proceso de extracción de datos almacenados en la web.

Objetivo: Recopilar información almacenada en un servicio web.

Aplicación: Productos, reseñas, noticias para hacer posteriormente un análisis.

---

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

## **¿Es legal?**
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