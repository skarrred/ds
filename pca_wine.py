import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load Wine Quality dataset
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target

# Perform PCA
pca = PCA()
pca_data = pca.fit_transform(df.drop('target', axis=1))

# Select appropriate number of principal components
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)

plt.figure(figsize=(10, 6))
plt.plot(cumulative_variance)
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance vs Number of Principal Components')
plt.show()

# Select the number of principal components based on the plot
n_components = 3

# Visualize the data in the reduced-dimensional space
pca_data_reduced = pca_data[:, :n_components]
plt.figure(figsize=(10, 6))
plt.scatter(pca_data_reduced[:, 0], pca_data_reduced[:, 1], c=df['target'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Wine Quality Data in Reduced-Dimensional Space')
plt.show()