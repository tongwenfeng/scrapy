#!/usr/bin/env python   
# -*- coding: UTF-8 -*-


import re
import json
import pymongo

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from douban.items import DoubanItem
from douban.download import download

class spider(CrawlSpider):
    name='m'
    #allowed_domains = ["http://music.douban.com"]
    start_urls=["http://music.douban.com/"]
    is_start=True

    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        items = []
        newurls = hxs.xpath("//a/@href").extract()
        rules = [
            #Rule(sle(allow=("subject/\d+/?$")),callback='parse2'),
            #Rule(sle(allow=("/tag/[^/]+/?$",)),callback='parse2'),
            #Rule(sle(allow=(".*douban.*",)),follow=True),
        ]
        #print url
        validurls =[]
        item=DoubanItem()
        for url in newurls:
            print url
            if True:
                validurls.append(url)
            regex_site=re.compile(r'.*site.*')
            #m = re.match(r".site.*",url)
            flag_site = regex_site.findall(url)
            if flag_site:
                #print url,m
                item['singerurl']=url
                item['singer']=' '
                yield  Request(item['singerurl'],meta={'item':item},callback=self.parse_item)
                newurls.remove(url)
            regex_tag = re.compile(r'http:music.douban.com/tag/.*')
            flag_tag = regex_tag.findall(url)
            if flag_tag:
                yield Request(url,callback=)
            n = re.compile(r'http:.*douban.*')
            t = n.findall(url)
            if t:
                yield Request(url,callback=self.parse)
        #items.extend([self.make_request_from_url(url).replace(callback=self.parse) for url in validurls])
    
    def parse2(self,response):
        hxs = HtmlXPathSelector
        items = []
        urls = hxs.select("//a/@href").extract()
        #print urls

    
    def parse_item(self,response):
        hxs=HtmlXPathSelector(response)
    	item=response.meta['item']
        #print item
        items=[]
        song=[]
        try:
            song=hxs.re("\[\{\"name\".*\]")
        except Exception as e:
            print e
        for s in song:
            record=json.loads(s)
            for b in record:
                #print '------------------------------'
                #print b['name'],b['rawUrl']
                dou = DoubanItem()
                dou['singer']=item['singer']
                dou['singerurl']=item['singerurl']
                dou['name'] = b['name']
                dou['url'] = b['rawUrl']
                #download(item['url'],item['name'])
                items.append(dou)
        print items
        #return items


    def parse_site(self,response):
        hxs = HtmlXPathSelector(response)
        items=[]
        for a in hxs.select("//div[@class=\"photoin\"]//a"):
            try:
                if re.match(".*",a.select("@href").extract()[0]) and re.match(".*",a.select("img//@alt").extract()[0]):
                    print a.select("@href").extract()[0],a.select("img//@alt").extract()[0]
                    item=DoubanItem()
                    item['singer']=a.select("img//@alt").extract()[0]
                    item['singerurl']=a.select("@href").extract()[0]
                    yield  Request(item['singerurl'],meta={'item':item},callback=self.parse_item)
            except Exception as e:
                pass
    
