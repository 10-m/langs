#!env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

num_points = 100
gradient = 0.5
x = np.array(range(num_points))
y = np.random.randn(num_points) * 10 + x*gradient
data = pd.DataFrame({'dummy x':x, 'dummy y':y})

data = pd.DataFrame({'dummy x':x, 'dummy y':y})
sns.lmplot('dummy x', 'dummy y', data,
           size=4, aspect=2)
plt.tight_layout()
plt.savefig('mpl_scatter_seaborn.png')
