#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_json(open('../data/nobel_winners.json'))
print(df.info())
print(df.describe())
print(df.describe(include=['object']))
print(df.head(2))
