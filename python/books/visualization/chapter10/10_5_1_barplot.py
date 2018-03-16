#!env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib  as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

labels = ["Physics", "Chemistry", "Literature", "Peace"]
foo_data = [3, 6, 10, 4]
bar_data = [8, 3, 6, 1]
fig, ax = plt.subplots(figsize=(8, 4))
bar_width = 0.4
xlocs = np.arange(len(foo_data))
ax.bar(xlocs-bar_width, foo_data, bar_width,
       color='#fde0bc', label='Fooland')
ax.bar(xlocs, bar_data, bar_width, color='peru', label='Barland')

#--- 目盛り、ラベル、グリッド、タイトル
ax.set_yticks(range(12))
ax.set_xticks(ticks=range(len(foo_data)))
ax.set_xticklabels(labels)
ax.yaxis.grid(True)
ax.legend(loc='best')
ax.set_ylabel('Number of prizes')
fig.suptitle('Prizes by country')
fig.tight_layout(pad=2) # ?
fig.savefig('mpl_barchart_multi.png', dpi=200)
