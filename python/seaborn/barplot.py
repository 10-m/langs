#!env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

df = pd.DataFrame({
  'Gender': ['Male', 'Female', 'Non-binary'],
  'Mean Satisfaction': [7.2, 8.1, 6.8]
})
print(df)
sns.barplot(
  data= df,
  x= "Gender",
  y= "Mean Satisfaction"
)
plt.savefig('barplot.png')
plt.close('all')

gradebook = pd.read_csv("data/gradebook.csv")
print(gradebook)
# sns.barplot(data=gradebook, x="assignment_name", y="grade")
sns.barplot(data=gradebook, x="student", y="grade")
plt.savefig('barplot2.png')
plt.close('all')

sns.barplot(data=gradebook,
            x="student",
            y="grade", ci="sd")
plt.savefig('barplot3.png')
plt.close('all')

sns.barplot(data=gradebook,
            x="student",
            y="grade", estimator=np.mean)
plt.savefig('barplot4.png')
plt.close('all')

sns.barplot(data=gradebook, x="student", y="grade", hue="assignment_name")
plt.savefig('barplot5.png')
plt.close('all')
