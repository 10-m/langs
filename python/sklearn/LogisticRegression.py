#!env python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import LogisticRegression

hours_studied_scaled = np.array([[-1.64750894],
                                 [-1.47408695],
                                 [-1.30066495],
                                 [-1.12724296],
                                 [-0.95382097],
                                 [-0.78039897],
                                 [-0.60697698],
                                 [-0.43355498],
                                 [-0.26013299],
                                 [-0.086711],
                                 [0.086711],
                                 [0.26013299],
                                 [0.43355498],
                                 [0.60697698],
                                 [0.78039897],
                                 [0.95382097],
                                 [1.12724296],
                                 [1.30066495],
                                 [1.47408695],
                                 [1.64750894]])
passed_exam = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1])

model = LogisticRegression()
model.fit(hours_studied_scaled, passed_exam)
calculated_coefficients = model.coef_
intercept = model.intercept_
print(calculated_coefficients)
print(intercept)

guessed_hours_scaled = np.array([[ -1.30066495e+00],
                                 [ -1.30066495e+00],
                                 [ -9.53820966e-01],
                                 [ -7.80398973e-01],
                                 [ -7.80398973e-01],
                                 [ -7.80398973e-01],
                                 [ -6.06976979e-01],
                                 [ -2.60132991e-01],
                                 [ -2.60132991e-01],
                                 [ -8.67109970e-02],
                                 [  8.67109970e-02],
                                 [  8.67109970e-02],
                                 [  2.60132991e-01],
                                 [  6.06976979e-01],
                                 [  6.06976979e-01],
                                 [  9.53820966e-01],
                                 [  1.47408695e+00],
                                 [  1.64750894e+00],
                                 [  3.31669563e+02]])
passed_predictions = model.predict_proba(guessed_hours_scaled)
print(passed_predictions)

passed_predictions_2 = model.predict(guessed_hours_scaled)
print(passed_predictions_2)
