#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'date_of_birth':'8 October 1927', 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'date_of_birth':'July 23, 1906', 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'date_of_birth':'1910-02-10', 'country':'ghi *'}
    ])
#print(pd.to_datetime(df.date_of_birth, errors='raise'))

df2 = pd.DataFrame.from_dict([
     {'name': 'Albert Einstein', 'category':'Physics', 'date_of_birth':'8 October 1927', 'country':'abc'},
     {'name': 'Marie Curie', 'category':'Chemistry', 'date_of_birth':'July 23, 1906', 'country':'def'},
     {'name': 'William Faulkner', 'category':'Literature', 'date_of_birth':'aaa', 'country':'ghi *'}
    ])
#print(pd.to_datetime(df2.date_of_birth, errors='raise'))

for i, row in df2.iterrows():
    try:
        print(pd.to_datetime(row.date_of_birth, errors='raise'))
    except:
        #print("{0} {1}", format(row.date_of_birth.ljust(30), row['name']))
        print("{0}({1}, {2:d})".format(row.date_of_birth.ljust(30), row['name'], i))


