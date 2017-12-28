#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':'123', 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':'456', 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':'', 'country':'ghi *'}
    ])

print(df)
print(df['year'].count())
df['year'].replace('', np.nan, inplace=True)
print(df)
print(df['year'].count())

print(df[df.country.str.contains('\*')]['country'])
df.country = df.country.str.replace('*', '')
df.country = df.country.str.strip()
print(df)
