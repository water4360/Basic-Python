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


#가시화를 위한 맷플롯립 figure만들기
fig = plt.figure(figsize=(10,7))
ax = plt.axes(projection = "3d")
# 3차원 공간에 데이터 가시화
ax.scatter3D(X[:,0], X[:,1], X[:,2], color = "green")
plt.title("3D scatter plot of Dataset")
plt.show()


