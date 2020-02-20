#!env python3
# -*- coding: utf-8 -*-
import os

file = 'tmp.txt';
# write
with open(file, 'w', encoding='utf-8') as fp:
    fp.write('1\n')

# append
with open(file, 'a', encoding='utf-8') as fp:
    fp.write('2\n')
    fp.write('3\n')

# writelines
data = ['a', 'b', 'c']
with open(file, 'a') as fd:
    fd.writelines([d + '\n' for d in data])

# read
with open(file, encoding='utf-8') as fp:
    s = fp.read()
    print(s, end='')

# readline
with open(file, encoding='utf-8') as fp:
    for i in range(2):
        s = fp.readline().rstrip()
        print(s)

# readlines
with open(file, encoding='utf-8') as fp:
    for s in fp.readlines():
        print(s.rstrip())

# read 1 line
with open(file, encoding='utf-8') as fp:
    for s in fp:
        print(s.rstrip())

os.remove(file)
