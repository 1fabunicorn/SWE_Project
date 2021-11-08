import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header
from dotenv import load_dotenv
import os

class ShopifyMollySpider(scrapy.Spider):
    name = 'shopify_molly'
    allowed_domains = ['www.mollyjogger.com']

    urls = [
        'https://www.mollyjogger.com/collections/inventory',
    ]
    load_dotenv()
    def start_requests(self):
        for url in self.urls:
            #yield scrapy.Request(url=url, callback=self.parse)
            yield SplashRequest(url, self.parse, endpoint='render.html', args={'wait': 2},
                                splash_headers={'Authorization': basic_auth_header(os.getenv('SPLASH_API_KEY'), '')})

    def parse(self, response):
        for item in response.css(".product"):
            yield {
                "name": item.css(".product-title::text").get(),
                "price": item.css(".price .money::text").get()
            }