#retor manejo de errores
import resquets
from bs4 import BeautifulSoup

url='https://www.pagina12.com.ar'

def obtener_notas(soup):
    lista_notas = []

    #obtengo el articulo promocionado
    feature_article = soup.find ('div', attrs={'class':'featured-aarticle'})