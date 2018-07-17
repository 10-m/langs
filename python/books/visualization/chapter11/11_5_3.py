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
df_temp=df[df.age_at_death.notnull()]
data = pd.DataFrame(
    {'age at death':df_temp.age_at_death,
     'date of birth':df_temp.date_of_birth / (1000*60*60*24*365) + 1700})
fig = sns.lmplot('date of birth',
                 'age at death',
                 data,
                 size=6,
                 aspect=1.5)
fig.savefig("11_5_3.png")
