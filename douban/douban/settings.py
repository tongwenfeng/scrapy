# Scrapy settings for douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'
SCHEDULER_ORDER = 'BFO'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['douban.pipelines.DoubanPipeline',]
EXTENTIONS = {
        'scrapy.contrib.corestats.CoreStats':0,
        'douban.statstodb.StatsToMongo':1000,
        }

REDIRECT_ENABLED = False
REDIRECT_MAX_TIMES = 0
MONGODB = {'host':'localhost','port':27017,'name':'track'}
