#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:11:33 2018

@author: duilio
"""

#from sklearn.datasets import load_iris
#
#iris = load_iris()
#print(iris.data.shape)
#print(iris.target_names)
#
#from sklearn import neighbors, datasets
#iris = datasets.load_iris()
#X, y = iris.data, iris.target
#knn = neighbors.KNeighborsClassifier(n_neighbors=1)
#knn.fit(X, y)
## What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
#print(iris.target_names[knn.predict([[3, 5, 4, 2]])])4

from sklearn.datasets import load_digits

digits = load_digits()

for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')