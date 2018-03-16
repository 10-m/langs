#!env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib  as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()
y = np.random.randn(200, 3).cumsum(0)

x = pd.period_range(pd.datetime.now(), periods=200, freq='d')
x = x.to_timestamp().to_pydatetime()

fig = plt.figure(
    figsize=(8, 4),  # インチ単位の図サイズ
    dpi=200,  # 1 インチ当たりのドット
    tight_layout=True,  # 軸やラベルなどをキャンバスに合わせる
    linewidth=1,
    edgecolor='r'  # 1 ピクセル幅、赤の境界
)
fig.tight_layout()
plt.plot(x, y)
plt.savefig("graph3.png")

fig = plt.figure(figsize=(8,4))
# --- 主軸
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_title('Main Axes with Insert Child Axes')
ax.plot(x, y[:,0])      # ?
ax.set_xlabel('Date')
ax.set_ylabel('Cum. sum')
# --- 挿入する軸
ax = fig.add_axes([0.15, 0.15, 0.3, 0.3])
ax.plot(x, y[:,1], color='g') # green（緑）の「g」
ax.set_xticks([]);      # ?

#fig.tight_layout()
plt.plot(x, y)
plt.savefig("graph4.png")


figure, ax = plt.subplots()
plots = ax.plot(x, y, label='')
figure.set_size_inches(8, 4)
ax.legend(plots, ('foo', 'bar', 'baz'), loc='best', framealpha=0.25,
prop={'size':'small', 'family':'monospace'})
ax.set_title('Random trends')
ax.set_xlabel('Date')
ax.set_ylabel('Cum. sum')
ax.grid(True)
figure.text(0.995, 0.01, u'\u00a9 Acme Designs 2015',
ha='right', va='bottom')
figure.tight_layout()
plt.savefig("graph5.png")

fig, axes = plt.subplots(
    nrows=3,
    ncols=1,
    sharex=True,
    sharey=True,
    figsize=(8, 8))
labelled_data = zip(
    y.transpose(),
    ('foo', 'bar', 'baz'),
    ('b', 'g', 'r'))
fig.suptitle('Three Random Trends', fontsize=16)
for i, ld in enumerate(labelled_data):
    ax = axes[i]
    ax.plot(x, ld[0], label=ld[1], color=ld[2])
    ax.set_ylabel('Cum. sum')
    ax.legend(loc='upper left', framealpha=0.5, prop={'size': 'small'})
axes[-1].set_xlabel('Date')
plt.savefig("graph6.png")
