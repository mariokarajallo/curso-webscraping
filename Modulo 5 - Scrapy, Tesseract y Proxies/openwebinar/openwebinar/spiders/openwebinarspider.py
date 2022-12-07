import scrapy


class OpenwebinarspiderSpider(scrapy.Spider):
    name = 'openwebinarspider'
    allowed_domains = ['openwebinars.net']
    start_urls = ['https://openwebinars.net/cursos/?page=1']

    def parse(self, response):
        cursos = response.xpath('//div[contains(@class, "card-course")]//*/a/@href').getall()

        for curso in cursos:
            yield response.follow(f"https://openwebinars.net{curso}", callback=self.parse_videos)
            
        paginas = response.xpath("//a[contains(@class, 'endless_page_link page-link')]/text()").getall()
        ultima_pagina = max([*map(int, paginas)])
        current_url = response.url
        index = current_url.index("=")+1
        base_url = current_url[:index]
        current_page = int(current_url[index:])

        if current_page < ultima_pagina:
            print(f'Pagina actual {current_page}')
            yield response.follow(f'{base_url}{current_page+1}')
