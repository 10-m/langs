#!env python3
# -*- coding: utf-8 -*-

import json

nobel_winners = [{
    'category': 'physics',
    'name': 'Albert Einstein',
    'nationality': 'Swiss',
    'sex': 'male',
    'year': 1921
}, {
    'category': 'physics',
    'name': 'Paul Dirac',
    'nationality': 'British',
    'sex': 'male',
    'year': 1933
}, {
    'category': 'chemistry',
    'name': 'Marle Curie',
    'nationality': 'Polish',
    'sex': 'female',
    'year': 1911
}]

with open('../data/nobel_winners.json', 'w') as f:
     json.dump(nobel_winners, f)

with open('../data/nobel_winners.json') as f:
    print(f.read())

nobel_winners = ''
with open('../data/nobel_winners.json') as f:
    nobel_winners = json.load(f)
print(nobel_winners)
