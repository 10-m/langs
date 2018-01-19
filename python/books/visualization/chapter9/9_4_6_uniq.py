#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':123, 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':456, 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':1911, 'country':'ghi *'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':1912, 'country':'ghi *'}
    ])

df.loc[(df.name == u'William Faulkner') & (df.year == 1911),
       'country'] = 'France'
print(df)
