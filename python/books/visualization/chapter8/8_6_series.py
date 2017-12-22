#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 4]) # Series(np.arange(4))
print(s)

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

s = pd.Series({'a':1, 'b':2, 'c':3})
print(s)

s = pd.Series({'a':1, 'b':2}, index=['a', 'b', 'c'])
print(s)

s = pd.Series({'a':1, 'b':2, 'c':3}, index=['a', 'b'])
print(s)

print(pd.Series(9, {'a', 'b', 'c'}))

s = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
print(np.sort(s))

print(s[1:3])

print(pd.Series([1, 2.1, 'foo']) + pd.Series([2, 3, 'bar']))

names = pd.Series(['Albert Einstein', 'Marie Curie'], name='name')
categories = pd.Series(['Physics', 'Chemistry'], name='category')
print(pd.concat([names, categories], axis=1))
