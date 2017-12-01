#!env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

nobel_winners = [{
    'category': 'Physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921
}, {
    'category': 'Physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1933
}, {
    'category': 'Chemistry',
    'name': 'Marie Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1911
}]

client = MongoClient('localhost', 27017)
db = client.nobel_prize
coll = db.winners

coll.insert(nobel_winners)
print(nobel_winners)

res = coll.find({'category':'Chemistry'})
print(list(res))

res = coll.find({'year':{'$gt':1930}}, {'sex':'female'})
print(list(res))

