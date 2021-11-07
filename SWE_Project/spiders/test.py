import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        yield {
            'title': response.css('h1::text').get(),
            'description': response.css('p::text').get(),
            'link': response.css('a::attr(href)').get()
        }
