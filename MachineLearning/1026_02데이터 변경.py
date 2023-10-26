import numpy as np
import matplotlib.pyplot as plt

u = np.array([1,1,1]) / np.sqrt(3)
v = np.array([1,0,-1]) / np.sqrt(2)

#1000개의 데이터 셋 생성
n_data = 1000
X = []
for _ in range(n_data):
    r_coeff = np.random.randn(2,)
    data = 2.0 * r_coeff[0] * u + r_coeff[1] * v + 0.1 * np.random.rand(3,)
    X.append(data)

X = np.array(X)
# print(X)



from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_2d_sklearn = pca.fit_transform(X)
plt.scatter(X_2d_sklearn[:, 0], X_2d_sklearn[:, 1], color='r')
plt.show()
