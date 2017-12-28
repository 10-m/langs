#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_json(open('../data/nobel_winners.json'))
print(df.columns)

df = df.set_index('name')
print(df)

nationalities = df['nationality']
print(nationalities)
print(type(nationalities))

print(df.iloc[0])

df = pd.read_json(open('../data/nobel_winners.json'))
df.set_index('name', inplace=True)
print(df.loc['Albert Einstein'])

print(df[0:2])
print(df[-1:])

mask = df.year > 1930
print(mask)
winners_since_1930 = df[mask]
print(winners_since_1930.count())
