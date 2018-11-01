#!env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

a = np.random.normal(40, 10, size=10000)
b = np.random.normal(60, 10, size=10000)

plt.figure()
plt.hist(a, bins=20, alpha=0.4, normed=True)
plt.hist(b, bins=20, alpha=0.4, normed=True)
plt.savefig('histgrame.png')
plt.close('all')
