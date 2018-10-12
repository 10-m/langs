#!env python3
# -*- coding: utf-8 -*-
import pandas as pd

print('--- Inner Merge II')
sales = pd.read_csv('data/sales.csv')
targets = pd.read_csv('data/targets.csv')

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets['revenue'] > sales_vs_targets['target']]
print(crushing_it)

print('--- Inner Merge III')
sales = pd.read_csv('data/sales.csv')
targets = pd.read_csv('data/targets.csv')
men_women = pd.read_csv('data/men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)
print(all_data)

results = all_data[(all_data['revenue'] > all_data['target']) & (all_data['women']> all_data['men'])]
print(results)

print('--- Merge on Specific Columns')
orders2 = pd.read_csv('data/orders2.csv')
products = pd.read_csv('data/products.csv')
orders_products = pd.merge(orders2, products.rename(columns={'id':'product_id'}))
print(orders_products)

print('--- Merge on Specific Columns II')
orders_products = pd.merge(orders2, 
                           products,
                           left_on='product_id',
                           right_on='id',
                           suffixes=['_orders','_products'])
print(orders_products)

print('--- Mismatched Merges')
merged_df = orders2.merge(products)
print(merged_df)

print('--- Outer Merge')
print(pd.merge(orders2, products, how='outer'))

print('--- Left and Right Merge')
print(pd.merge(orders2, products, how='right'))

print('--- Concatenate DataFrames')
df1 = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df2 = pd.DataFrame([
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df3 = pd.concat([df1, df2]).reset_index()
print(df1)
print(df2)
print(df3)
