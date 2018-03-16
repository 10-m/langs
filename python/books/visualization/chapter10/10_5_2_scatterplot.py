#!env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib  as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points) * 10 + x*gradient
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x, y)
fig.suptitle('A Simple Scatterplot')
fig.tight_layout(pad=2)
fig.savefig('scatterplot.png', dpi=200)
