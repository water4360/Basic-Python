import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#01.
iris = load_iris()
df = pd.DataFrame(data = np.c_[iris['data'], iris['target']],
                  columns = iris['feature_names'] + ['target'])
print(df)


#02. 4차원 데이터의 2차원화
from sklearn.preprocessing import StandardScaler
features = iris['feature_names']
x = df.loc[:, features].values #특징
y = df.loc[:,['target']].values # 레이블
x = StandardScaler().fit_transform(x)

#03. PCA 적용
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(x)
principalDf = pd.DataFrame(data = pca_result, columns = ['PC1', 'PC2'])

#04. 새로운 데이터프레임 생성
finalDF = pd.concat([principalDf, df[['target']]], axis = 1)
# print(finalDF)

#05. 데이터 가시화
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Primary Principal Component')
ax.set_ylabel('Secondary Principal Component')
ax.set_title('Dimension Reduction with PCA', fontsize = 20)
targets = [0.0, 1.0, 2.0]
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    idx = finalDF['target'] == target
    ax.scatter(finalDF.loc[idx, 'PC1'], finalDF.loc[idx, 'PC2'], c = color)
ax.legend(targets)
ax.grid()
plt.show()