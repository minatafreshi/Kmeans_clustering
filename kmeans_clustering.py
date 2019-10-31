import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataset = pd.read_csv('')
X = dataset.iloc[:,[,]].values

# Add kmeans to dataset

kmeans = KMeans(n_clusters= , init= '', random_state= )
Y = kmeans.fit_predict(X)

plt.scatter(X[Y == 0, 0], X[Y == 0,1], s = 100, c = 'green', label = 'cluster 1')

plt.scatter(X[Y == 1, 0], X[Y == 1,1], s = 100, c = 'red', label = 'cluster 2')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', label = 'Centroids')

plt.title('kmeans clustering')
plt.xlabel('attribute 1')
plt.ylabel('attribute 2')
plt.legend()
plt.show()