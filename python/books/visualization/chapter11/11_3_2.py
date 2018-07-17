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

new_index = pd.Index(np.arange(1901, 2015), name='year')
by_year_gender = df.groupby(['year','gender'])
year_gen_sz = by_year_gender.size().unstack().reindex(new_index)

fig, axes = plt.subplots(nrows=2, ncols=1,
            sharex=True, sharey=True)
ax_f = axes[0]
ax_m = axes[1]

fig.suptitle('Nobel Prize-winners by gender', fontsize=16)
ax_f.bar(year_gen_sz.index, year_gen_sz.female)
ax_f.set_ylabel('Female winners')
ax_m.bar(year_gen_sz.index, year_gen_sz.male)
ax_m.set_ylabel('Male winners')
ax_m.set_xlabel('Year')

##fig = year_gen_sz.plot(kind='bar', figsize=(16,4)).get_figure()
fig.savefig("11_3_2.png")

def thin_xticks(ax, tick_gap=10, rotation=45):
    """ x 目盛りを減らし、回転を調整する """
    ticks = ax.xaxis.get_ticklocs()
    ticklabels = [l.get_text()\
                  for l in ax.xaxis.get_ticklabels()]
    ax.xaxis.set_ticks(ticks[::tick_gap])
    ax.xaxis.set_ticklabels(ticklabels[::tick_gap],\
                            rotation=rotation)
    ax.figure.show()
