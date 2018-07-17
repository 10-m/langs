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
by_cat_gen = df.groupby(['category', 'gender'])
print(by_cat_gen.get_group(('Physics', 'female'))[['name','year']])
print(by_cat_gen.size())
fig = by_cat_gen.size().plot(kind='bar').get_figure()
fig.savefig("11_3.png")
