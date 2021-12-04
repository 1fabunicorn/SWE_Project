import scrapy
from scrapy_selenium import SeleniumRequest
from urllib.parse import urlparse, parse_qs, urljoin
from src.ClassEnumeration import ClassEnumeration

from scrapy.utils.response import open_in_browser


class EnnumeratingSpider(scrapy.Spider):
    name = 'default'
    # allowed_domains = ['www.adoredvintage.com']

    enumeration = ClassEnumeration()

    urls = ["https://partakefoods.com", "https://uppercasemagazine.com", "https://hiutdenim.co.uk",
            "https://www.manitobah.com", "https://packagefreeshop.com", "https://flourist.com",
             "https://www.allbirds.com", "https://www.naja.co", "https://unitedbyblue.com", "https://bailly.co",
             "https://www.givemetap.com", "https://www.silkandwillow.com", "https://www.tazachocolate.com", "https://www.smartypits.com",
            "https://www.makergear.com", "https://www.parklandmfg.ca", "https://www.thehoneypot.co", "https://www.goodfair.com", "https://www.lunchskins.com"]
    # urls = ['https://www.deathwishcoffee.com/collections/coffee']

    def start_requests(self):
        for url in self.urls:
            yield SeleniumRequest(url=url + "/collections/all", callback=self.parse,
                                  script='window.scrollTo(0,document.body.scrollHeight);')

    def parse(self, response):
        count = 0
        yield {
            "results": self.enumeration.get(response)
        }
        # for item in response.css(".product-collection__content"):
        #     count += 1
        #     yield {
        #         "name": item.css(".product-collection__content h4 a:first-child::text").get(),
        #         #"description": item.css(".product-collection__description p::text").get(),
        #         "price": item.css(".product-collection__price span span::text").get()
        #     }

        if count > 0: # Dynamic pagination
            urlparams = parse_qs(urlparse(response.url).query)
            newpage = 2
            if "page" in urlparams:
                newpage = int(urlparams["page"][0]) + 1
            yield response.follow(urljoin(response.url, "?page=" + str(newpage)), callback=self.parse)

        #     #button = response.css(".pagination span span a::attr(href)").get()
        #     #if button is not None:
        #          #yield response.follow(button, callback=self.parse)
