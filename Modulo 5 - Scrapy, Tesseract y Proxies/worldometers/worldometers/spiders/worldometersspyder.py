import scrapy


class WorldometersspyderSpider(scrapy.Spider):
    name = 'worldometersspyder'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/']

    def parse(self, response):
        pass
