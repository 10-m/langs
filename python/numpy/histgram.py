#!env python3
# -*- coding: utf-8 -*-
import numpy as np

exercise_ages = np.array([22, 27, 45, 62, 34, 52, 42, 22, 34, 26, 24, 65, 34, 25, 45, 23, 45, 33, 52, 55])
print(np.histogram(exercise_ages, range = (20, 70), bins = 5))

