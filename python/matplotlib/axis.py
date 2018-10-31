#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]

plt.figure()
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.savefig('axis.png')
plt.close('all')
