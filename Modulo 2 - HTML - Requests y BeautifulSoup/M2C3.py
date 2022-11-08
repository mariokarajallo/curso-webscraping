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