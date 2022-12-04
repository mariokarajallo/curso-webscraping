
import scrapy

class Spider12(scrapy.Spider):
    # nombre del scraper nombre igual a la clase, nombre de nuestra araña.
    name = 'spiderpagina12'
    # que dominios queremos scrapear, lo que no este definido aqui no va a scrapear
    allowed_domains = ['paginas12.com.ar']
    # fomato que queremos nos genere el archivo de salida
    # permite configurar el archivo de salida
    custom_settings = {
        'FEEDS': {
                'pagina12dic.json': {
                    'format': 'json',
                    'encoding': 'UTF-8',
                },
        },
        # 'DEPTH_LIMIT': 2,
    }
    # definimos URLS de INICIO
    # URLs para comenzar a rastrear
    # start_urls = ['https://www.pagina12.com.ar/secciones/deportes']
    start_urls = 'https://www.pagina12.com.ar/secciones/deportes'

    '''
    Nuestra araña ya tiene un método start_requests() implementado por defecto, que se encarga de generar una respuesta por cada una de estas URLs y de enviarla al método callback por defecto denominado parse.
    '''

    '''
    el rastreador llama a este método de callback, pasándole los objetos de respuesta de las páginas como argumento. En el método parse nos encargaremos de extraer la información que queramos de cada URL mediante expresiones XPaths, expresiones regurales (REgex) o selectores CSS.
    '''
    def parse_notas(self, response):
        print('-------------------')
        print(response.url)
        print('-------------------')

    def parse(self, response):
        # url base
        # url_base = 'https://www.pagina12.com.ar'

        # recibe de la respuesta de las urls definidas anteriormente

        # extraemos el articulo Promocionado
        # nota_promocionada = response.xpath(
        #     '//article[@class="article-item article-item--main "]//h2/a/@href').get()

        # si obtuvimos el link a la nota promocionada llamamos a parse_nota
        # y automaticamente scrapy le pasa la respuesta (response)
        # if nota_promocionada is not None:
        #     # seguimos el link de articulo promocionado y procesamos la respuesta con un callback a parse_not
        #     nota_promocionada = urljoin(url_base, nota_promocionada)
        #     yield response.follow(nota_promocionada, self.parse_nota)

        # lista de todas las notas no procionadas
        urls=[]
        notas = response.xpath(
            '//section[@class="list-content"]//h3//a/@href|//section[@class="list-content"]//h4//a/@href').getall()
        for nota in notas:
            # print('Pagina deportes')
            # nota = urljoin(url_base, nota)
            # print(f' estoy aca {nota}')
            urls.append('https://www.pagina12.com.ar'+nota)
        
        print ('dic url ',urls)
        
        for i in urls:
            # print('URL: ',i)
            yield response.follow(i, callback=self.parse_notas)

        # link siguiente paguina
        # next_page_url = response.xpath(
        #     '//div[@class="articles-list-pager"]//a[@class="next"]/@href').get()
        # if next_page_url:
        #     yield response.follow(f'https://www.pagina12.com.ar/{next_page_url}', self.parse)

    


    # def parse_nota(self, response):
    #     # extraemos el titulo de la nota
    #     titulo = response.xpath('//article/div[1]/div[2]/h1/text()').get()
    #     # extraemos la fecha de la nota
    #     fecha = response.xpath(
    #         '//article/div[2]/div[1]/div/div[1]/span/time/text()').get()

    #     yield {'url': response.url,
    #            'titulo': titulo,
    #            'fecha': fecha}

# process = CrawlerProcess()
# process.crawl(Spider12)
# process.start()