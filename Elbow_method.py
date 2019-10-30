import numpy as np
import pandas as ps 
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Importing the dataset

dataset = ps.read_cvs('')
X = dataset.iloc[:,[,]].values

# Using Elbow Method for finding right number of clusters

sum_squares = []

for in range (,):
    Kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    Kmeans.fit(X)
    sum_squares.append(Kmeans.inertia_)

# Visualize the Elbow method with Plot

plt.plot(range(,), sum_squares)
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.show()
