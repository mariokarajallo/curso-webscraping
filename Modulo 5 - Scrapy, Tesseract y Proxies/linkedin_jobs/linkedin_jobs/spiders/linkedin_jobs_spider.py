import scrapy


class LinkedinJobsSpiderSpider(scrapy.Spider):
    name = 'linkedin_jobs_spider'
    api_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=python&location=United%2BStates&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&start=' 
    # allowed_domains = ['linkedin.com']
    # start_urls = ['http://linkedin.com/']

    def start_requests(self):
        first_job_on_page = 0
        first_url = self.api_url + str(first_job_on_page)
        yield scrapy.Request(url=first_url, callback=self.parse_job, meta={'first_job_on_page': first_job_on_page})
