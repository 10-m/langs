#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':np.nan, 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':'456', 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'year':'', 'country':'ghi *'}
    ])

print(df)
print(df.year.isnull())
print(df.drop('year', axis=1))
