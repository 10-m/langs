#!env python3
# -*- coding: utf-8 -*-

import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
print(test_1)

test_2 = np.genfromtxt('data/test_2.csv', delimiter=',')
print(test_2)

print('--- Operations with NumPy Arrays')
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2
print(test_3_fixed)

total_grade = test_1 + test_2 + test_3_fixed
print(total_grade)

final_grade = total_grade / 3
print(final_grade)

print('--- Two-Dimensional Arrays')
coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[1, 0, 0, 1, 0],
                            [0, 0, 1, 1, 1]])
print(coin_toss_again)

print('--- Selecting Elements from a 1-D Array')
jeremy_test_2 = test_2[3]
print(jeremy_test_2)
manual_adwoa_test_1 = test_1[1:3]
print(manual_adwoa_test_1)

print('--- Selecting Elements from a 2-D Array')
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])
tanya_test_3 = student_scores[2, 0]
cody_test_scores = student_scores[:,4]

print('--- Logical Operations with Arrays')
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge < 60]
print(cold)
hot = porridge[porridge > 80]
print(hot)
just_right = porridge[(porridge >= 60) & (porridge <= 80)]
print(just_right)
