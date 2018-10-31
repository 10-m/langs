#!env python3
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

x=[i for i in range(12)]
y1=[i * 2 for i in range(12)]
y2=[i * 3 for i in range(12)]

plt.figure()
plt.plot(x, y1, color = 'pink', marker='o', linestyle='--')
plt.plot(x, y2, color = 'gray', marker='o')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(['y1', 'y2'], loc='lower right')
plt.savefig('introduction.png')
plt.close('all')
