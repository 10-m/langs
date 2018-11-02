#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, autopct='%1d%%', labels=unit_topics)
plt.axis('equal')
plt.title("Hardest Topics")
plt.savefig('pie.png')
plt.close('all')
