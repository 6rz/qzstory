# -*- coding: utf-8 -*-
import scrapy
from qzstory.items import QzstoryItem

class qzSpider(scrapy.Spider):
    name = 'qzspider'
    allowed_domains = ['http://www.gushi365.com/']
    start_urls = [
        'http://www.gushi365.com/',
    ]

#    def start_requests(self):  
#        yield scrapy.Request("http://www.gushi365.com/", headers={'User-Agent': "Hello"})

    def parse(self, response):
        item = QzstoryItem()

        item['story_title'] = response.xpath('//article/figure/a/img/@alt').extract()
        item['story_url'] = response.xpath('//article/figure/a/@href').extract()            
        yield item  
  
        for url in item['story_url']:  
            print url  
            url = "http://www.gushi365.com/" + url  
#            yield scrapy.Request(url, callback=self.parse_story,dont_filter=True,headers={'User-Agent': "Hello"})  
            yield scrapy.Request(url, callback=self.parse_story,dont_filter=True,) 
    def parse_story(self, response):
        item = QzstoryItem()
        item['story_content'] = response.xpath('//div[@class="single-content"]/span/p/text()').extract()
        self.log('ITEM :: %s' % (item['story_content']))
        return item
        

            