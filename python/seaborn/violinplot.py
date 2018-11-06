#!env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

n = 10000
a = np.random.normal(40, 30, size=n)
b = np.random.normal(60, 20, size=n)
c = np.random.normal(80, 10, size=n)

df = pd.DataFrame({
    "label": ["a"] * n + ["b"] * n + ["c"] * n,
    "value": np.concatenate([a, b, c])
})

sns.set_style("darkgrid")
sns.set_palette("pastel")

sns.violinplot(data=df, x="label", y="value")

plt.savefig('violinplot.png')
plt.close('all')
