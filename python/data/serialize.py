#!env python3
# -*- coding: utf-8 -*-
import shelve

with shelve.open('shelve.db') as db:
    db['name'] = 'python'
    db['dict'] = {"A": 3, "B": (2, 5), "C": "Hello"} 
    db['list'] = [2,4,5,6,1,2,3]

with shelve.open('shelve.db') as db:
    print(db['name'])
    print(db['dict'])
    print(db['list'])
