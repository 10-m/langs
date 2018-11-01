#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.figure()
plt.pie(payment_method_freqs, autopct = '%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
plt.savefig('pie.png')
plt.close('all')
