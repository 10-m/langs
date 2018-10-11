#!env python3
# -*- coding: utf-8 -*-
import pandas as pd

print('--- Calculating Column Statistics')
orders = pd.read_csv('data/orders.csv')
print(orders.head(10))
print(orders['price'].max())
print(orders['shoe_color'].nunique())

print('--- Calculating Aggregate Functions I')
pricey_shoes = orders.groupby('shoe_type')['price'].max()
print(pricey_shoes)
print(type(pricey_shoes))

print('--- Calculating Aggregate Functions II')
pricey_shoes = orders.groupby('shoe_type')['price'].max().reset_index()
print(pricey_shoes)
print(type(pricey_shoes))

print('--- Calculating Aggregate Functions III')
import numpy as np
cheap_shoes = orders.groupby('shoe_color')['price'].apply(lambda x: np.percentile(x, 25)).reset_index()
print(cheap_shoes)

print('--- Calculating Aggregate Functions IV')
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()
print(shoe_counts.head(10))

print('--- Pivot Tables')
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
print(shoe_counts.head(10))
shoe_counts_pivot = shoe_counts.pivot(columns = 'shoe_color',
                                      index = 'shoe_type',
                                      values='id').reset_index()
print(shoe_counts_pivot)
