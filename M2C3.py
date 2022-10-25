# reto-extrayendo-informacion

import requests
from bs4 import BeautifulSoup
# obtenemos la pagina de donde extraemos la informacion
pagina = requests.get('https://www.pagina12.com.ar/secciones/el-pais')

#parseamos la pagina
soup = BeautifulSoup(pagina.text, 'lxml')

def obtener_notas(soup):
    '''
    Función que recibe un objeto de BeautifulSoup de una página de una sección 
    y devuelve una lista de URLs a las notas de esa sección
    '''
    # creamos un array de todos los elementos con el tag article que tengan el atributo class=article-item
    article_items = soup.find_all('article', attrs={'class':'article-item'})

    #recorremos el array y obtemos los elementos que cumplan la condicion
    article_links = [item.a.get('href') for item in article_items]
    
    return article_links


print (obtener_notas(soup))