#!env python3
# -*- coding: utf-8 -*-
import csv
import sqlite3
import os
import sqlalchemy as sa

test1 = 'This is a test of the emergency text system'
with open('test.txt', 'wt') as fh:
    fh.write(test1)

with open('test.txt', 'rt') as fh:
    for line in fh:
        print(line)

csv_text1 = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''

with open('books1.csv', 'wt') as fh:
    fh.write(csv_text1)

with open('books1.csv', 'rt') as fh:
    cin = csv.DictReader(fh)
    books = [row for row in cin]
print(books)

csv_text2 = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books2.csv', 'wt') as fh:
    fh.write(csv_text2)

db_name = 'books.db'
if os.path.exists(db_name):
    os.remove(db_name)
conn = sqlite3.connect(db_name)
curs = conn.cursor()
create_query = '''CREATE TABLE book
 (title VARCHAR(20) PRIMARY KEY, author VARCHAR(20), year INT)'''
curs.execute(create_query)

with open('books2.csv', 'rt') as fh:
    cin = csv.DictReader(fh)
    ins = 'INSERT INTO book (title, author, year) VALUES(?, ?, ?)'
    for row in cin:
        curs.execute(ins, (row['title'], row['author'], row['year']))

curs.execute('SELECT title FROM book ORDER BY title')
titles = curs.fetchall()
print(titles)

curs.execute('SELECT * FROM book ORDER BY year')
rows = curs.fetchall()
print(rows)
conn.commit()
curs.close()
conn.close()

# conn = sa.create_engine('sqlite:///books.db', echo=True)
conn = sa.create_engine('sqlite:///books.db')
rows = conn.execute('SELECT title FROM book ORDER BY title')
for row in rows:
    print(row)
