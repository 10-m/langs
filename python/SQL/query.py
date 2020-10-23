#!env python3
# -*- coding: utf-8 -*-
import sqlite3
import os
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
    create = 'CREATE TABLE movies (id INT, name TEXT, genre TEXT, year INT, imdb_rating FLOAT)'
    print(create)
    c.execute(create)

    insert = 'INSERT INTO movies (id, name, genre, year, imdb_rating) VALUES (?,?,?,?,?)'
    print(insert)
    recoreds = [(1, 'Avatar', 'action', 2009, 7.9),
                (2, 'Jurassic World', 'action', 2015, 7.3),
                (51, 'Shrek 2', 'comedy', 2004, 7.2),
                (52 , 'Toy Story 3', 'comedy', 2010, 8.4),
                (219, 'Se7en', 'drama', 1995 , 8.6),
                (220, 'Seven', 'drama', 1979 , 6.1)]
    c.executemany(insert, recoreds)

    insert = 'INSERT INTO movies (id, name, genre, year) VALUES (?,?,?,?)'
    recoreds = [(222, 'Dawn of the Dead', 'horror', 1978),
                (223, 'Shawn of the Dead', 'comedy', 2004)]
    c.executemany(insert, recoreds)
    conn.commit()

    select = 'SELECT * FROM movies'
    print_and_exec(select, c)

    select = 'SELECT name, genre  FROM movies'
    print_and_exec(select, c)

    select = 'SELECT name AS "Title"  FROM movies'
    print_and_exec(select, c)

    select = 'SELECT DISTINCT genre FROM movies'
    print_and_exec(select, c)

    select = 'SELECT * FROM movies WHERE id IN (1, 51)'
    print_and_exec(select, c)

    select = 'SELECT * FROM movies WHERE year > 2009'
    print_and_exec(select, c)

    select = 'SELECT * FROM movies WHERE name LIKE "Se_en"'
    print_and_exec(select, c)

    select = 'SELECT * FROM movies WHERE name LIKE "S%"'
    print_and_exec(select, c)

    select = 'SELECT * FROM movies WHERE imdb_rating IS NULL'
    print_and_exec(select, c)

    select = '''
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
'''
    print_and_exec(select, c)

    select = '''
SELECT * 
FROM movies
WHERE year < 1985 AND genre = 'horror';
'''
    print_and_exec(select, c)

    select = '''
SELECT *
FROM movies
WHERE genre = 'action'
   OR genre = 'comedy';
'''
    print_and_exec(select, c)

    select = '''
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;
'''
    print_and_exec(select, c)

    select = '''
SELECT *
FROM movies
ORDER BY imdb_rating DESC LIMIT 3;
'''
    print_and_exec(select, c)

    select = '''
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END
FROM movies;
'''
    print_and_exec(select, c)

if os.path.exists(dbname):
    os.remove(dbname)
