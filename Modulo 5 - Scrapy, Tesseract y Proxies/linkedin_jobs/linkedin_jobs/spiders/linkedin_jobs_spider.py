import scrapy


class LinkedinJobsSpiderSpider(scrapy.Spider):
    name = 'linkedin_jobs_spider'
    allowed_domains = ['linkedin.com']
    start_urls = ['http://linkedin.com/']

    def parse(self, response):
        pass
