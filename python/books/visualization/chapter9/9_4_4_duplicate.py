#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':np.nan, 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':'456', 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':'', 'country':'ghi *'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':'', 'country':'ghi *'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':'', 'country':'ghi *'}
    ])

print(df.duplicated('name'))
print(df.duplicated('name', keep='last'))

dupes_by_name = df[df.duplicated('name')]
print(df.name.isin(dupes_by_name.name))

for name, rows in df.groupby('name'):
    print('name: %s, number of rows: %d'%(name, len(rows)))

print(pd.concat([g for _, g in df.groupby('name') if len(g) > 1])['name'])
