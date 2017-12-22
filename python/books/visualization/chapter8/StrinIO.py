#!env python3
# -*- coding: utf-8 -*-

from io import StringIO
import pandas as pd

data = " `Albert Einstein`| Physics \n`Marie Curie`| Chemistry"
df = pd.read_csv(
    StringIO(data),
    sep='|',
    names=['name', 'category'],
    skipinitialspace=True,
    quotechar="`")
print(df)
