#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import json
import seaborn as sb

plt.rcParams['figure.figsize'] = 8, 4

df = pd.read_json('../data/nobel_winners_biopic_cleaned.json')
by_gender = df.groupby('gender')
fig = by_gender.size().plot(kind='bar').get_figure()
fig.savefig("fist.png")
print(by_gender.size())
