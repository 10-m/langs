#!env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

a = np.random.normal(40, 10, size=10000)
b = np.random.normal(60, 10, size=10000)

plt.figure(figsize=(10,8))
plt.hist(a, bins=12, normed=True, histtype='step', linewidth=2)
plt.hist(b, bins=12, normed=True, histtype = 'step',linewidth=2)
plt.legend(["1st Yr Teaching", "2nd Yr Teaching"])
plt.title("Final Exam Score Distribution")
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.savefig('histgrame.png')
plt.close('all')
