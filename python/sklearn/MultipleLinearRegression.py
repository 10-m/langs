#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("data/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms',
        'bathrooms',
        'size_sqft',
        'min_to_subway',
        'floor',
        'building_age_yrs',
        'no_fee',
        'has_roofdeck',
        'has_washer_dryer',
        'has_doorman',
        'has_elevator',
        'has_dishwasher',
        'has_patio',
        'has_gym']]
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    train_size = 0.8,
                                                    test_size = 0.2,
                                                    random_state = 6)

mlr = LinearRegression()
model=mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

print(mlr.coef_)
print(mlr.score(x_train, y_train))
print(mlr.score(x_test, y_test))

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.scatter(y_test, y_predict, alpha=0.4)
fig1.savefig('mlr_satter1.png')

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.scatter(df[['size_sqft']], df[['rent']], alpha=0.4) 
fig2.savefig('mlr_satter2.png')
