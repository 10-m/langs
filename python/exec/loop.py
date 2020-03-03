#!env python3
# -*- coding: utf-8 -*-

items = ('cup', 'art', 'box')
print('items:', items)

# range
print(list(range(10)))
print(list(range(1, 11)))

# enumerate
print(list(enumerate(items)))
print(list(enumerate(items, start=1)))

# zip
print(list(zip(range(3), items)))

# sorted
print(sorted(items))

# reversed
print(list(reversed(items)))
