# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from src.ClassEnumeration import ClassEnumeration


class SweProjectPipeline:
    enumeration = ClassEnumeration()

    def open_spider(self, spider):
        self.file = open('items.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_enumerating_spider(self, item):
        # an item is a single line representing text under the targeted classes. We need to clean
        s = item.strip()
        self.file.write(s)
        self.file.write("\n")
        return s

    def process_item(self, item, spider):
        if spider.name == 'default':
            for r in item['results']:  # different css selections from the class enumeration
                item["results"] = self.process_enumerating_spider(r)
        return item
