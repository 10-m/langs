#!env python3
# -*- coding: utf-8 -*-
import pandas as pd
import glob

print('--- Dealing with Multiple Files')
student_files = glob.glob('data/exams*.csv')
df_list = []
for file in student_files:
    data = pd.read_csv(file)
    df_list.append(data)

students = pd.concat(df_list)
print(len(students))

print('--- Reshaping your Data')
print(students.columns)
students = pd.melt(frame=students,
                   id_vars=['full_name','gender_age','grade'],
                   value_vars=['fractions', 'probability'],
                   value_name='score',
                   var_name='exam')
print(students.head())
print(students.columns)
print(students.exam.value_counts())

print('--- Dealing with Duplicates')
duplicates = students.duplicated()
print(duplicates.value_counts())

students = students.drop_duplicates()
duplicates = students.duplicated()
print(duplicates.value_counts())

print('--- Dealing with Duplicates')
students['gender'] = students.gender_age.str[0]
students['age'] = students.gender_age.str[1:]
print(students.head())
students = students[[column for column in students.columns if column != "gender_age"]]

print('--- Splitting by Character')
students['name_split'] = students['full_name'].str.split(' ')
students['first_name'] = students['name_split'].str.get(0)
students['last_name'] = students['name_split'].str.get(1)
print(students.head())

print('--- Looking at Types')
print(students.dtypes)

print('--- String Parsing')
students.score = students['score'].replace('[\%,]', '', regex=True)
students.score = pd.to_numeric(students['score'])
print(students.score[0])

print('--- More String Parsing')
students['grade'] = pd.to_numeric(students['grade'].replace('th.*$', '', regex=True))
print(students.dtypes)
avg_grade = students['grade'].mean()
print(str(avg_grade) + 'th grade')

print('--- Missing Values')
score_mean = students['score'].mean()
print(score_mean)
students['score'] = students['score'].fillna(0)
score_mean_2 = students['score'].mean()
print(score_mean_2)
