#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'year':1234},
     {'name': 'Marie Curie', 'category':'Chemistry', 'year':5678},
     {'name': 'William Faulkner', 'category':'Literature', 'year':90}
    ])

print(set(df.year.apply(type)))


