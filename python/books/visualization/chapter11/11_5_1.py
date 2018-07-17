#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import json
import seaborn as sns

df = pd.read_json('../data/nobel_winners_biopic_cleaned.json')
fig = df['award_age'].hist(bins=20).get_figure()
sns.distplot(df['award_age']).get_figure()
fig.savefig("11_5_1.png")

sns.boxplot(df.gender, df.award_age)
fig.savefig("11_5_1_2.png")

sns.violinplot(df.gender, df.award_age)
fig.savefig("11_5_1_3.png")
