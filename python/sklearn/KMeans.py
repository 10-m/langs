#!env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
samples = iris.data
target = iris.target

### Implementing K-Means: Scikit-Learn
model = KMeans(n_clusters=3)
model.fit(samples)
labels = model.predict(samples)
print(labels)

### New Data?
new_samples = np.array([[5.7, 4.4, 1.5, 0.4],
                        [6.5, 3. , 5.5, 0.4],
                        [5.8, 2.7, 5.1, 1.9]]) 
print(new_samples)
# Predict labels for the new_samples
print(model.predict(new_samples))

### Visualize After K-Means
x = samples[:,0]
y = samples[:,1]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y, c=labels, alpha=0.5)
fig.savefig('visualize_after_kmeans.png')

### Evaluation
species = np.chararray(target.shape, itemsize=150)
for i in range(len(samples)):
  if target[i] == 0:
    species[i] = 'setosa'
  elif target[i] == 1:
    species[i] = 'versicolor'
  elif target[i] == 2: 
    species[i] = 'virginica'

df = pd.DataFrame({'labels': labels, 'species': species})
print(df.head(10))
ct = pd.crosstab(df['labels'], df['species'])
print(ct)

### The Number of Clusters
num_clusters = [i for i in range(1, 9)]
inertias = []
for k in num_clusters:
  model = KMeans(n_clusters=k)
  model.fit(samples)
  inertias.append(model.inertia_)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(num_clusters, inertias, '-o')
ax.set_xlabel('Number of Clusters (k)')
ax.set_ylabel('Inertia')
fig.savefig('number_of_clusters.png')
