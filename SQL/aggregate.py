#!env python3
# -*- coding: utf-8 -*-
import sqlite3
import os
import re
from contextlib import closing

dbname = 'tmp.db'
if os.path.exists(dbname):
    os.remove(dbname)

def print_and_exec(select, c):
    print('---')
    print(select)
    for row in c.execute(select):
        print(row)

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    create = 'CREATE TABLE fake_apps (id INT, name TEXT, category TEXT, downloads INT, price FLOAT)'
    print(create)
    c.execute(create)

    insert = 'INSERT INTO fake_apps (id, name, category, downloads, price) VALUES (?,?,?,?,?)'
    print(insert)

    file = 'data/fake_apps.csv';
    with open(file, 'r') as fd:
        for line in fd:
            line = re.sub('\r?\n?$', '', line)
            items = line.split(',')
            c.execute(insert, items)
    conn.commit()

    select = 'SELECT COUNT(*) FROM fake_apps WHERE price = 0'
    print_and_exec(select, c)

    select = 'SELECT COUNT(*) FROM fake_apps'
    print_and_exec(select, c)

    select = 'SELECT MAX(price) FROM fake_apps'
    print_and_exec(select, c)

    select = 'SELECT AVG(price) FROM fake_apps'
    print_and_exec(select, c)

    select = 'SELECT ROUND(AVG(price),2) FROM fake_apps'
    print_and_exec(select, c)

    select = 'SELECT price, COUNT(*) FROM fake_apps GROUP BY price'
    print_and_exec(select, c)

    select = 'SELECT category, SUM(downloads) FROM fake_apps GROUP BY category'
    print_and_exec(select, c)

    select = 'SELECT category, price, AVG(downloads) FROM fake_apps GROUP BY 1, 2'
    print_and_exec(select, c)

    select = '''
SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(downloads) > 10
'''
    print_and_exec(select, c)

if os.path.exists(dbname):
    os.remove(dbname)
