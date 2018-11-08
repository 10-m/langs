#!env python3
# -*- coding: utf-8 -*-
import sqlite3
import os
from contextlib import closing

dbname = 'tmp.db'
if os.path.exists(dbname):
    os.remove(dbname)

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    create = 'CREATE TABLE celebs (id INT, name TEXT, age INT)'
    print(create)
    c.execute(create)

    insert = 'INSERT INTO celebs (id, name, age) VALUES (?,?,?)'
    print(insert)
    users = [(1, 'Justin Bieber', 22),
             (2, 'Beyonce Knowles', 33),
             (3, 'Jeremy Lin', 26),
             (4, 'Taylor Swift', 26)]
    c.executemany(insert, users)
    conn.commit()

    select_all = 'SELECT * FROM celebs'
    print(select_all)
    for row in c.execute(select_all):
        print(row)

    update = 'UPDATE celebs SET age = 23 WHERE id = 1'
    print(update)
    c.execute(update)
    for row in c.execute(select_all):
        print(row)

    alter_table = 'ALTER TABLE celebs ADD COLUMN twitter_handle TEXT'
    print(alter_table)
    c.execute(alter_table)
    for row in c.execute(select_all):
        print(row)

    update = "UPDATE celebs SET twitter_handle = '@taylorswift13' WHERE id = 4"
    print(update)
    c.execute(update)

    delete = "DELETE FROM celebs WHERE twitter_handle IS NULL"
    print(delete)
    c.execute(delete)
    for row in c.execute(select_all):
        print(row)

    create = '''
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        recipient TEXT NOT NULL,
        award_name TEXT DEFAULT 'Grammy')
    '''
    print(create)
    c.execute(create)
    insert = 'INSERT INTO awards (id, recipient) VALUES (?, ?)'
    award = (1, "xxx")
    print(insert, award)
    c.execute(insert, award)
    for row in c.execute('SELECT * FROM awards'):
        print(row)

