#!env python3
# -*- coding: utf-8 -*-

data = ['a', 'b', 'c']

file = 'tmp.txt';
with open(file, 'w') as fd:
    fd.writelines([d + '\n' for d in data])

