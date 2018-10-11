#!env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

print('--- Adding a Column I')
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

print('--- Adding a Column II')
df['Is taxed?'] = 'Yes'
print(df)

print('--- Adding a Column III')
df['Revenue'] = df['Price'] - df['Cost to Manufacture']
print(df)

print('--- Performing Column Operations')
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

df['Lowercase Name'] = df['Name'].apply(lambda x: x.lower())
print(df)

print('--- Reviewing Lambda Function')
mylambda = lambda x: x[0] + x[-1]
print(mylambda('This is a string'))

print('--- Reviewing Lambda Function: If Statements')
mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
print(mylambda(13))
print(mylambda(12))

print('--- Applying a Lambda to a Column')
df = pd.read_csv('data/employees.csv')
get_last_name = lambda x: x.split(' ')[1]
df['last_name'] = df['name'].apply(get_last_name)
print(df.head(5))

print('--- Applying a Lambda to a Row')
total_earned = lambda row: row['hours_worked'] * row['hourly_wage'] if row['hours_worked'] <= 40 else 40 * row['hourly_wage'] + 1.5 * row['hourly_wage'] * (row['hours_worked'] - 40)
df['total_earned'] = df.apply(total_earned, axis=1)
print(df.head(5))

print('--- Renaming Columns')
df = pd.read_csv('data/imdb.csv')
print(df.info())
df.columns = ['ID','Title','Category','Year Released','Rating']
print(df.info())

print('--- Renaming Columns II')
df = pd.read_csv('data/imdb.csv')
df.rename(columns={'name':'movie_title'}, inplace=True)
print(df.info())
