#!env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import json
import seaborn as sns

plt.rcParams['figure.figsize'] = 8, 4
plt.rcParams['font.size'] = 20

df = pd.read_json('../data/nobel_winners_biopic_cleaned.json')
new_index = pd.Index(np.arange(1901, 2015), name='year')

by_year_nat_sz = df.groupby(['year', 'country']).size().unstack().reindex(new_index).fillna(0)
fig = by_year_nat_sz['United States'].fillna(0).cumsum().plot().get_figure()
fig.savefig("11_4_3_1.png")

not_US = by_year_nat_sz.columns.tolist()
not_US.remove('United States')
by_year_nat_sz['Not US'] = by_year_nat_sz[not_US].sum(axis=1)
fig = by_year_nat_sz[['United States', 'Not US']].cumsum().plot().get_figure()
fig.savefig("11_4_3_2.png")

by_year_nat_sz = df.groupby(['year', 'country']).size().unstack().reindex(new_index).fillna(0)
regions = [
    {'label':'N. America',
     'countries':['United States', 'Canada']},
    {'label':'Europe',
     'countries':['United Kingdom', 'Germany', 'France']},
    {'label':'Asia',
     'countries':['Japan', 'Russia', 'India']}
]

for region in regions:
    by_year_nat_sz[region['label']] = by_year_nat_sz[region['countries']].sum(axis=1)

fig = by_year_nat_sz[[r['label'] for r in regions]].cumsum().plot().get_figure()
fig.savefig("11_4_3_3.png")

COL_NUM = 4
ROW_NUM = 4
by_nat_sz = df.groupby('country').size()
by_nat_sz.sort_values(ascending=False,inplace=True)
fig, axes = plt.subplots(COL_NUM, ROW_NUM,
                         sharex=True, sharey=True,
                         figsize=(12,12))

for i, nat in enumerate(by_nat_sz.index[1:17]):
    ax = axes[int(i/COL_NUM), i%ROW_NUM]
    by_year_nat_sz[nat].cumsum().plot(ax=ax)
    ax.set_title(nat)

fig.savefig("11_4_3_4.png")

bins = np.arange(df.year.min(), df.year.max(), 10)
by_year_nat_binned = df.groupby([pd.cut(df.year,
                                        bins,
                                        precision=0),
                                 'country']).size().unstack().fillna(0)
plt.figure(figsize=(8, 8))
fig = sns.heatmap( by_year_nat_binned[by_year_nat_binned.sum(axis=1) > 2]).get_figure()
fig.savefig("11_4_3_5.png")
