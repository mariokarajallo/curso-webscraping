import scrapy


class occSpider(scrapy.Spider):
    name = 'occSpider'
    allowed_domains = ["occidente.co"]
    custom_settings = { "FEED_FORMAT": "json",
                        "FEED_URI": "occidente.json",		 
                        "FEED_EXPORT_ENCODING": "utf-8",
                        "DEPTH_LIMIT": 10}
    start_urls = ["https://occidente.co/politica/"]


    def parse(self, response):
        news = response.xpath('//*//a[@class="text-black text-decoration-none"]/@href').getall()
        for n in news:
            yield response.follow(n, self.parse_news)

        for next_page in response.xpath('//*//div[@class="nav-links text-center mx-auto"]/div/a[contains(.,"Siguiente")]/@href'):
            yield response.follow(next_page, self.parse)
    

    def parse_news(self, response):
        title = response.xpath('//div[@class="container"]//h1[@class="main-post-title art-title font-family-judson font-size-48 font-weight-bold line-height-1em"]/text()').getall()
        body = response.xpath('*//div[@class="font-family-roboto font-size-18"]/p/text()').getall()
        yield {"url": response.url, 
               "title": title, 
               "body": body}
              
        for next_page in response.xpath('//nav/ul[@class="pager"]/li[@class="next"]/a/@href'):
            yield response.follow(next_page, self.parse)