#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import json
import seaborn as sns
import datetime

df = pd.read_json('../data/nobel_winners_biopic_cleaned.json')
df['age_at_death'] = (df.date_of_death - df.date_of_birth) / (1000*60*60*24*365)
age_at_death = df[df.age_at_death.notnull()].age_at_death
fig = sns.distplot(age_at_death, bins=40).get_figure()
fig.savefig("11_5_2.png")

df2 = df[df.age_at_death.notnull()]
sns.kdeplot(df2[df2.gender == 'male'].age_at_death, shade=True, label='male')
sns.kdeplot(df2[df2.gender == 'female'].age_at_death, shade=True, label='female')
fig2 = plt.legend().get_figure()
plt.figure()
fig2.savefig("11_5_2_2.png")

fig3 = sns.violinplot(df.gender, age_at_death).get_figure()
plt.figure()
fig3.savefig("11_5_2_3.png")
