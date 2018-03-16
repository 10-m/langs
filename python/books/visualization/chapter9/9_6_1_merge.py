#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df1 = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':123, 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':456, 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':1911, 'country':'ghi *'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':1912, 'country':'ghi *'}
    ])

df2 = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':123, 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':456, 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':1911, 'country':'ghi *'},
     {'name': 'William Faulkner1', 'category':'Literature', 'year':1912, 'country':'ghi *'}
    ])

print(pd.merge(df1, df2, how='outer'))
