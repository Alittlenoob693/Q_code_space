import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler


class KMeans:
    def __init__(self,cluter = 3,max_iter = 300,tol = 1e-4,init = "k-means++"):
        self.cluter = cluter
        self.max_iter = max_iter
        self.tol = tol
        self.centon = None
        self.init = init

    def init_centon(self,x):
        if self.init=="random":
            indit = np.random.choice(x.shape[0],self.cluter,replace=False)
            return x[indit]

        centon = []
        centon.append(x[np.random.randint(x.shape[0])])

        for _ in range(1,self.cluter):
            distances = np.min([np.linalg.norm(x - c,axis=1) for c in centon])
            probs = distances**2/np.sum(distances**2)
            chosen = np.random.choice(x.shape[0],p=probs)
            centon.append(x[chosen])

        return np.array(centon)


    def fit(self,x):
        self.centon = self.init_centon(x)
        for _ in range(1,self.max_iter):
            distances = np.linalg.norm(x[:,np.newaxis] - self.centon,axis=2)
            labels = np.argmin(distances,axis=1)
            new_centon = np.array(x[labels == i].mean(axis=0) for i in range(self.cluter))

            if np.linalg.norm(new_centon - self.centon) < self.tol:
                break

            self.centon = new_centon

        self.labels = labels



    def predict(self,x):
        distances = np.linalg.norm(x[:,np.newaxis] - self.centon,axis=2)
        return np.argmin(distances,axis=0)


df = pd.read_csv("iris.csv",header=None)
x = df.drop(["species"],axis=1)

scaler = StandardScaler()
scaler_x = scaler.fit_transform(x)

kmeans = KMeans(cluter=3,max_iter=300,tol=1e-4,init="random")
kmeans.fit(scaler_x)
labels = kmeans.labels
plt.scatter(scaler_x[:, 0], scaler_x[:, 1], c=labels, cmap='viridis', alpha=0.5)
plt.scatter(kmeans.centon[:, 0], kmeans.centon[:, 1], c='red', marker='x', s=100, label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('K-Means Clustering on Iris Dataset (CSV)')
plt.show()
