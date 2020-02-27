#!env python3
# -*- coding: utf-8 -*-

items = ('cup', 'art', 'box')
print('items:', items)

print('enumerate:')
print(list(enumerate(items)))

print('zip:')
print(list(zip(range(3), items)))

print('sorted:')
print(sorted(items))

print('reversed:')
print(list(reversed(items)))
