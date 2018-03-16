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

plt.plot(x, y)
plt.savefig("graph.png")

# Matplotlibの設定
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = 'r' # 赤

plots = plt.plot(x, y)

# ラベルと凡例
plt.legend(plots, ('foo', 'bar', 'baz'),        # ?
           loc='best',      # ?
           framealpha=0.5,  # ?
           prop={'size':'small', 'family':'monospace'}) # ?

# 図サイズを 8 × 4 インチに設定する
plt.rcParams['figure.figsize'] = (8,4)
plt.gcf().set_size_inches(8, 4)
           
# タイトルと軸ラベル
plt.title('Random trends')
plt.xlabel('Date')
plt.ylabel('Cum. sum')

# テキスト
plt.figtext(0.995, 0.01,
            u'c Acme designs 2015',
            ha='right', va='bottom')

# 保存
plt.tight_layout()
plt.savefig("graph2.png")
