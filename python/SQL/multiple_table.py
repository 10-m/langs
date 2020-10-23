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
    creates = ['CREATE TABLE customers (customer_id INT, customer_name TEXT, address TEXT)',
               'CREATE TABLE subscriptions (subscription_id INT, description TEXT, price_per_month INT, subscription_length TEXT)',
               'CREATE TABLE orders (order_id INT, customer_id INT, subscription_id INT, purchase_date DATE)']
    for create in creates:
        c.execute(create)

    inserts = ['INSERT INTO customers (customer_id, customer_name, address) VALUES (?,?,?)',
               'INSERT INTO subscriptions (subscription_id, description, price_per_month, subscription_length) VALUES (?,?,?,?)',
               'INSERT INTO orders (order_id, customer_id, subscription_id, purchase_date) VALUES (?,?,?,?)']
    files = ['data/customers.csv', 'data/subscriptions.csv', 'data/orders.csv']
    for insert, file in zip(inserts, files):
        with open(file, 'r') as fd:
            for line in fd:
                line = re.sub('\r?\n?$', '', line)
                items = line.split(',')
                c.execute(insert, items)
    conn.commit()

    tables = ['customers', 'subscriptions', 'orders']
    for table in tables:
        select = 'SELECT * FROM {} LIMIT 5'.format(table)
        print_and_exec(select, c)

    select = 'SELECT * FROM orders JOIN subscriptions ON orders.subscription_id = subscriptions.subscription_id'
    print_and_exec(select, c)

    select = '''
    SELECT *
        FROM orders
        JOIN subscriptions
        ON orders.subscription_id = subscriptions.subscription_id
        WHERE subscriptions.description = 'Fashion Magazine'
    '''
    print_and_exec(select, c)

    select = 'SELECT COUNT(*) FROM customers JOIN orders ON customers.customer_id = orders.customer_id'
    print_and_exec(select, c)

    select = 'SELECT * FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id'
    print_and_exec(select, c)

    select = 'SELECT * FROM customers CROSS JOIN orders'
    print_and_exec(select, c)

    select = 'CREATE TABLE orders2 AS SELECT * FROM orders'
    print_and_exec(select, c)

    select = 'UPDATE orders2 SET order_id = order_id + 20'
    print_and_exec(select, c)

    select = 'SELECT * FROM orders UNION SELECT * FROM orders2'
    print_and_exec(select, c)

if os.path.exists(dbname):
    os.remove(dbname)
