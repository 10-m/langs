#!env python3
# -*- coding: utf-8 -*-

import csv

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

with open('../data/nobel_winners2.csv', 'w') as f:
    fieldnames = nobel_winners[0].keys()
    fieldnames = sorted(fieldnames)
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in nobel_winners:
        writer.writerow(w)

with open('../data/nobel_winners2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('../data/nobel_winners2.csv') as f:
    reader = csv.DictReader(f)
    nobel_winners = list(reader)
print(nobel_winners)
