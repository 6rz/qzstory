# -*- coding: utf-8 -*-
import scrapy
from qzstory.items import QzStorysItem,QzStoryItem

class qzSpider(scrapy.Spider):
    name = 'qzspider'
    allowed_domains = ['http://www.gushi365.com']
    start_urls = [
        'http://www.gushi365.com/',
    ]

#    def start_requests(self):  
#        yield scrapy.Request("http://www.gushi365.com/", headers={'User-Agent': "Hello"})

    def parse(self, response):
        item = QzStorysItem()

        item['story_titles'] = response.xpath('//article/figure/a/img/@alt').extract()
        item['story_urls'] = response.xpath('//article/figure/a/@href').extract()
   
        yield item  
  
        for url in item['story_urls']: 
            title = item['story_titles'][item['story_urls'].index(url)]
            url = "http://www.gushi365.com" + url  
#            yield scrapy.Request(url, callback=self.parse_story,dont_filter=True,headers={'User-Agent': "Hello"})  
            yield scrapy.Request(url, callback=self.parse_story,dont_filter=True,meta={'title': title,'url': url}) 
    def parse_story(self, response):
        item = QzStoryItem()
        item['story_title'] =  response.meta['title'] 
        item['story_url'] =  response.meta['url']       
#        item['story_content'] = response.xpath('//div[@class="single-content"]/span/p/text()').extract()

        span =response.xpath('//div[@class="single-content"]/span')
        content=""
        for p in span.xpath('.//p/text()'):
            content = content+ p.extract()
            item['story_content'] = content
#        self.log('ITEM :: %s' % (item['story_content']))
        return item
        

            