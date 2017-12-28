#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df1 = pd.DataFrame({'foo': [1, 2, 3], 'bar':['a', 'b', 'c']})
print(df1)

df2 = pd.DataFrame({'baz': [7, 8, 9, 11], 'qux':['p', 'q', 'r', 't']})
print(df2)

pn = pd.Panel({'item1':df1, 'item2':df2})
print(pn)

print(pn['item1'])

