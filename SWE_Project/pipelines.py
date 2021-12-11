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

    def process_item(self, item, spider):
        if spider.name == 'default':
            pass
        return item
