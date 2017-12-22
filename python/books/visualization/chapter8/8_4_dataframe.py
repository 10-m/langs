#!env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_json('../data/nobel_winners.json')
print(df)
print(df.columns)
print(df.index)

df2 = df.set_index('name')
print(df2)
print(df2.loc['Albert Einstein'])

print(df.iloc[2])

gender_col = df['sex']
print(type(gender_col)) 
print(gender_col.head())

df3 = df.groupby('category')
print(df3.groups.keys())

phy_group = df3.get_group('physics')
print(phy_group.head())

print(df['category'] == 'physics')
print(df[df['category'] == 'physics'])

