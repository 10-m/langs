#!env python3
# -*- coding: utf-8 -*-

import csv
import trace

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

def main():
    cols = nobel_winners[0].keys()
    cols = sorted(cols)
    with open('../data/nobel_winners.csv', 'w') as f:
        f.write(','.join(cols) + '\n')
        for o in nobel_winners:
            row = [str(o[col]) for col in cols]
            f.write(','.join(row) + '\n')

    with open('../data/nobel_winners.csv') as f:
        for line in f.readlines():
            print(line)

tracer = trace.Trace()
tracer.runfunc(main)
r = tracer.results(trace=0, count=0, countfuncs=1)
r.write_results(show_missing=True, coverdir=".")
