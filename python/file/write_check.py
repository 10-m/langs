#!env python3
# -*- coding: utf-8 -*-

file = 'tmp.txt'
try:
    with open(file, 'x') as fd:
        fd.write('Hello' + '\n')
except FileExistsError:
    print(file + ' exits already')
