#!env python3
# -*- coding: utf-8 -*-
import numpy as np

print('--- NumPy and Mean')
store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)
print(store_one_avg)
print(store_two_avg)
print(store_three_avg)

print('--- Mean and Logical Operations')
print(np.mean(store_two > 7))

print('--- Calculating the Mean of 2D Arrays')
allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

total_mean = allergy_trials.mean()
print(total_mean)

trial_mean = allergy_trials.mean(axis=1)
print(trial_mean)

patient_mean = allergy_trials.mean(axis=0)
print(patient_mean)

print('--- Sorting and Outliers')
heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])
print(np.sort(heights))

print('--- NumPy and Median')
my_array = np.array([50, 38, 291, 59, 14])
print(np.median(my_array))

print('--- Percentiles')
movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])
first_quarter = np.percentile(movies_watched, 25)
print(first_quarter)
third_quarter = np.percentile(movies_watched, 75)
print(third_quarter)
interquartile_range = third_quarter - first_quarter
print(interquartile_range)

print('--- NumPy and Standard Deviation')
nums = np.array([65, 36, 52, 91, 63, 79])
print(np.std(nums))

