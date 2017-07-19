# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas
import sqlite3
import json

class QzStoryPipeline(object):
    def process_item(self, item, spider):
        if item.get('story_titles')or item.get('story_urls'): 
            line = json.dumps(dict(item))
            df = pandas.read_json(line.decode("unicode_escape"))
            df.to_excel("story.xlsx",sheet_name='Sheet1')
        
            with sqlite3.connect('qzstorys.sqlite') as db:
                df.to_sql('qzstorys',con = db)
        return item
