# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QzStorysItem(scrapy.Item):
    story_titles = scrapy.Field()
    story_urls = scrapy.Field()    
    pass

class QzStoryItem(scrapy.Item):
    story_title = scrapy.Field()
    story_url = scrapy.Field()    
    story_content = scrapy.Field()     
    pass
