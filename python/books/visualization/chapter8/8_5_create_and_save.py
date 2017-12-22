#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame({
     'name': ['Albert Einstein', 'Marie Curie',\
     'William Faulkner'],
     'category': ['Physics', 'Chemistry', 'Literature']
     })
print(df)

df = pd.DataFrame.from_dict([{
    'name': 'Albert Einstein',
    'category': 'Physics'
}, {
    'name': 'Marie Curie',
    'category': 'Chemistry'
}, {
    'name': 'William Faulkner',
    'category': 'Literature'
}])
print(df)

print(df.head())
