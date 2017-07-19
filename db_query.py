# -*- coding: utf-8 -*-
import pandas
import sqlite3
import json        
        
with sqlite3.connect('qzstorys.sqlite') as db:
    df = pandas.read_sql_query('SELECT * FROM qzstorys',con = db)
    print df