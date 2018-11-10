# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 21:46:30 2018

@author: cyy24
"""

import sqlite3

con = sqlite3.connect('knowledge_base.db')
c = con.cursor()

statement1 = '''
CREATE TABLE knowledge(
knowledge_id   int          PRIMARY KEY    ,
knowledge_name varchar(50),
knowledge      text,
category_id    int,
FOREIGN KEY(category_id) REFERENCES category(category_id)   
)'''

statement2 = '''CREATE TABLE category(    
category_id    int    PRIMARY KEY,
category_name  varchar(50) 
)
'''

c.execute(statement1)
c.execute(statement2)