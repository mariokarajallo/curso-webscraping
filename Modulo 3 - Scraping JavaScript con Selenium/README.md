# Curso de Web Scraping: Extracción de Datos en la Web

# **Modulo III - Scraping JavaScript con Selenium**
- [Clase 11 Instalación y configuración de Selenium](#11-instalación-y-configuración-de-selenium)

## 11. **Instalación y configuración de Selenium** 

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

## 12. ** ** 