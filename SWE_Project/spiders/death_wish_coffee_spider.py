import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header
from dotenv import load_dotenv
import os


class death_wish_coffee_spider(scrapy.Spider):
    name = "Death Wish Coffee"
    urls = [
        'https://www.deathwishcoffee.com/collections/coffee',
    ]
    http_user = "MzNlMjczYWMzNzkzNGUyNzhjMTIwZDY0NjNjY2NiNzQ6"
    load_dotenv()
    def start_requests(self):
        for url in self.urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args={'wait': 2},
                                splash_headers={'Authorization': basic_auth_header(os.getenv('SPLASH_API_KEY'), '')})

    def parse(self, response):
        for item in response.css(".product-hero-card__item-title"):
            yield {
                "content": item.get()
            }
