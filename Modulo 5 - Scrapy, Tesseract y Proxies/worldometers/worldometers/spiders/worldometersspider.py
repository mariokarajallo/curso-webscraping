import scrapy


class WorldometersspyderSpider(scrapy.Spider):
    name = 'worldometersspider'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # selecionamos la tabla
        rows = response.xpath('//tr')

        for row in rows:    
            #title = response.xpath('//h1/text()').get()        
            countries = row.xpath('./td/a/text()').get()
            population=row.xpath('./td[3]/text()').get()

            yield{
                #'title': title,
                'countries':countries,
                'population':population
            }