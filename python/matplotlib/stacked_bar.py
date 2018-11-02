#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

plt.figure(figsize=(10,8))
plt.bar(range(len(As)), As)
plt.bar(range(len(Bs)), Bs, bottom = As)
plt.bar(range(len(Cs)), Cs, bottom = c_bottom)
plt.bar(range(len(Ds)), Ds, bottom = d_bottom)
plt.bar(range(len(Fs)), Fs, bottom = f_bottom)
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title("Grade distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")
plt.savefig('stacked_bar.png')
