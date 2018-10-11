#!env python3
# -*- coding: utf-8 -*-
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ["t-shirt", "t-shirt", "skirt", "skirt"],
  'Color': ['blue', 'green', 'red', 'black']
  # add Product Name and Color here
})
print(df1)

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  # Fill in rows 3 and 4
  [3, "San Francisco", 90],
  [4, "Sacramento", 115]
],
  columns=[
    "Store ID", "Location", "Number of Employees"
  ])
print(df2)

df = pd.read_csv('data/cupcakes.csv')
print(df)
print('--- head')
print(df.head())
print('--- info')
print(df.info())

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df['clinic_north']
print('--- type')
print(type(clinic_north))
print(type(df))

clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))

print('--- Select Rows')
march = df.iloc[2]
print(march)

print('--- Selecting Multiple Rows')
april_may_june = df.iloc[3:]
print(april_may_june)

print('--- Select Rows with Logic I')
january = df[df.month == "January"]
print(january)

print('--- Select Rows with Logic II')
march_april = df[(df.month == 'March') | (df.month == 'April')]
print(march_april)

print('--- Select Rows with Logic III')
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)

print('--- Setting indices')
df2 = df.loc[[1, 3, 5]]
print(df2)

df3 = df2.reset_index()
print(df3)

df2.reset_index(inplace=True, drop=True)
print(df2)
