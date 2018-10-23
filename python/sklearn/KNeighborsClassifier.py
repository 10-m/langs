#!env python3
# -*- coding: utf-8 -*-

import re
from sklearn.neighbors import KNeighborsClassifier

movie_dataset = []
dataset_file = 'data/movie_dataset.csv';
with open(dataset_file, 'r') as fd:
    for line in fd:
        line = re.sub('\r?\n?$', '', line)
        movie_dataset.append(line.split(','))

labels = []
lables_file = 'data/movie_labels.txt'
with open(lables_file, 'r') as fd:
    line = fd.readline()
    line = re.sub('\r?\n?$', '', line)
    labels = line.split(',')

classifier = KNeighborsClassifier(n_neighbors = 5)
classifier.fit(movie_dataset, labels)
guesses = classifier.predict([[.45, .2, .5], [.25, .8, .9],[.1, .1, .9]])
print(guesses)
