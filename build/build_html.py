# -*- coding: utf-8 -*-
import pandas
import sqlite3
import json        
import sys

# UnicodeEncodeError: 'ascii' codec can't //通过以下语句修改编码设置解决
reload(sys)
sys.setdefaultencoding( "utf-8" )
        
with sqlite3.connect('..\qzstorys.sqlite') as db:
    df = pandas.read_sql_query('SELECT * FROM qzstory',con = db)
    for i in range(0,len(df)):
        with open(df['story_title'][i]+'.html',"w") as file:
            str =  """
            <html>
            <head>
            <meta charset="utf-8">
            <title>QzStory</title>
            </head>
            <body>
               <p>%s</p>
            </body>
            </html>
            """ % (df['story_content'][i],)
            file.write(str)
