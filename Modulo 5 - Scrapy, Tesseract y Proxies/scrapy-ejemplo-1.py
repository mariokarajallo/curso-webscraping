# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class Spider12(scrapy.Spider):
    #nombre del scraper nombre igual a la clase, nombre de nuestra araña.
    name='spider12'
    #que dominios queremos scrapear, lo que no este definido aqui no va a scrapear
    allowed_domains=['paginas12.com.ar']
    #fomato que queremos nos genere el archivo de salida
    #permite configurar el archivo de salida
    custom_settings={
        'FEEDS': {
                'notas_pagina12.json': {
                    'format': 'json',
                    'encoding': 'UTF-8',
                    'overwrite': True
                },
        },
        'DEPTH_LIMIT': 2,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }   
    # definimos URLS de INICIO
    # URLs para comenzar a rastrear
    start_urls=['https://www.pagina12.com.ar/secciones/el-pais',
    'https://www.pagina12.com.ar/secciones/economia',
    'https://www.pagina12.com.ar/secciones/sociedad',
    'https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos',
    'https://www.pagina12.com.ar/secciones/deportes',
    'https://www.pagina12.com.ar/secciones/ciencia',
    'https://www.pagina12.com.ar/secciones/el-mundo',
    'https://www.pagina12.com.ar/edicion-impresa',
    'https://www.pagina12.com.ar/secciones/universidad-diario',
    'https://www.pagina12.com.ar/secciones/ajedrez',
    'https://www.pagina12.com.ar/secciones/cultura',
    'https://www.pagina12.com.ar/secciones/dialogos',
    'https://www.pagina12.com.ar/secciones/plastica',
    'https://www.pagina12.com.ar/secciones/psicologia',
    'https://www.pagina12.com.ar/secciones/cartas-de-lectores',
    'https://www.pagina12.com.ar/secciones/contratapa',
    'https://www.pagina12.com.ar/secciones/audiovisuales',
    'https://www.pagina12.com.ar/secciones/recordatorios',
    'https://www.pagina12.com.ar/secciones/consumo',
    'https://www.pagina12.com.ar/secciones/buenos-aires12',
    'https://www.pagina12.com.ar/secciones/salta12',
    'https://www.pagina12.com.ar/secciones/catamarca12',
    'https://www.pagina12.com.ar/secciones/la-rioja12',
    'https://www.pagina12.com.ar/secciones/podcasts',
    'https://www.pagina12.com.ar/secciones/soci@s',
    'https://www.pagina12.com.ar/secciones/la-ventana']

    '''
    Nuestra araña ya tiene un método start_requests() implementado por defecto, que se encarga de generar una respuesta por cada una de estas URLs y de enviarla al método callback por defecto denominado parse.
    '''

    '''
    el rastreador llama a este método de callback, pasándole los objetos de respuesta de las páginas como argumento. En el método parse nos encargaremos de extraer la información que queramos de cada URL mediante expresiones XPaths, expresiones regurales (REgex) o selectores CSS.
    '''
    def parse(self, response):
        # recibe de la respuesta de las urls definidas anteriormente

        #extraemos el articulo Promocionado
        nota_promocionada= response.xpath('//article[@class="article-item article-item--main"]//h2/a/@href').get()

        #si obtuvimos el link a la nota promocionada llamamos a parse_nota
        # y automaticamente scrapy le pasa la respuesta (response) 
        if nota_promocionada is not None:
            #seguimos el link de articulo promocionado y procesamos la respuesta con un callback a parse_not
            yield response.follow(nota_promocionada, callback=self.parse_nota)

        #lista de todas las notas no procionadas
        notas = response.xpath('//section[@class="list-content"]//h3//a/@href|//section[@class="list-content"]//h4//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback=self.parse_nota)

        #link siguiente paguina
        next_page_url=response.xpath('//div[@class="articles-list-pager"]//a[@class="next"]/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)

    
    def parse_nota(self, response):
        #extraemos el titulo de la nota
        titulo = response.xpath('//article/div[1]/div[2]/h1/text()').get()
        if titulo:
            titulo=titulo
        else:
            titulo=None

        #extraemos la fecha de la nota
        fecha = response.xpath('//article/div[2]/div[1]/div/div[1]/span/time/text()').get()
        if fecha:
            fecha=fecha
        else:
            fecha=None

        yield dict(url=response.url, titulo=titulo, fecha=fecha)