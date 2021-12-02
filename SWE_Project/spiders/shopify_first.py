import scrapy
from scrapy_splash import SplashRequest
from w3lib.http import basic_auth_header
import os

from urllib.parse import urlparse, parse_qs, urljoin

class ShopifySpider(scrapy.Spider):
    name = 'shopify_first'
    allowed_domains = ['www.adoredvintage.com']


    urls = ['https://www.adoredvintage.com/collections/all'] #Website 12
    def start_requests(self):
        for url in self.urls:
            #yield scrapy.Request(url=url, callback=self.parse)
            yield SplashRequest(url, self.parse, endpoint='render.html', args={'wait': 2},
                                splash_headers={'Authorization': basic_auth_header(os.getenv('SPLASH_API_KEY'), '')})

    def parse(self, response):
        count = 0
        for item in response.css(".product-collection__content"):
            count = count + 1
            yield {
                "name": item.css(".product-collection__content h4 a:first-child::text").get(),
                #"description": item.css(".product-collection__description p::text").get(),
                "price": item.css(".product-collection__price span span::text").get()
            }
        #Dynamic pagination
        if count > 0:

            urlparams = parse_qs(urlparse(response.url).query)

            newpage = 2
            if "page" in urlparams:
                newpage = int(urlparams["page"][0]) + 1

            yield response.follow(urljoin(response.url, "?page=" + str(newpage)), callback=self.parse)

            #button = response.css(".pagination span span a::attr(href)").get()

            #if button is not None:
                 #yield response.follow(button, callback=self.parse)