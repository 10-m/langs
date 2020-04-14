#!env python3
# -*- coding: utf-8 -*-
import os

print(os.path.join('aaa', 'bbb'))
print(os.path.exists(__file__))
print(os.path.isfile(__file__))
print(os.path.isdir(__file__))

for name in os.listdir('.'):
    print(name)

for root, dirs,files in os.walk('.'):
    print(root)
    for dir in dirs:
        print('\t', dir)
    for file in files:
        print('\t\t', file)
