#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df2 = pd.DataFrame(
     {'name':['zak', 'alice', 'bob', 'mike', 'bob', 'bob'],
      'score':[4, 3, 5, 2, 3, 7]})
print(df2)

print(df2.sort_values(['name', 'score'], ascending=[1, 0]))

