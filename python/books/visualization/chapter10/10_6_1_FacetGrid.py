#!env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips, col="smoker")
g.map(plt.scatter, "total_bill", "tip")

pal = dict(Female='red', Male='blue')
g = sns.FacetGrid(
    tips,
    col="smoker",
    hue="sex",
    hue_kws={"marker": ["D", "s"]},  # ?
    palette=pal,
    size=4,
    aspect=1, )
g.map(plt.scatter, "total_bill", "tip", alpha=.4)
g.add_legend()
g.savefig('facet_grid.png')
