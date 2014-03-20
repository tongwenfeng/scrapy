# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from douban.db import mongo
from datetime import datetime
#from scrapy.contrib.pipeline.images import ImagesPipeline



class DoubanPipeline(object):
    def __init__(self) :
        self.date = datetime.now().strftime("%Y-%m-%d-%H:%M")
    def process_item(self, item, spider):
        if 'DoubanItem' is item.__class__.__name__:
            self.process_douban_item(item)
        return item
    def process_douban_item(self,item):
        item.update({'date':self.date})
        if mongo.getdb().music.find({'name':item['name'],'singer':item['singer']}).count() is 0:
            mongo.getdb().music.insert(dict(item))
        else:
            mongo.getdb().music.update({'name':item['name']},dict(item))
