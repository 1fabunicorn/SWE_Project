import scrapy
from scrapy_selenium import SeleniumRequest


class selenium_spider(scrapy.Spider):
    name = "selenium"
    url = 'https://www.deathwishcoffee.com/collections/coffee'

    def start_requests(self):
        yield SeleniumRequest(url=self.url, callback=self.parse)

    def parse(self, response):
        for item in response.css(".product-hero-card__item-title"):
            yield {
                "content": item.get()
            }
