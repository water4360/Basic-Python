import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
data = np.vstack((v1, v2))
print(data) #[[1 2 3]/[4 5 6]]
print()
data2 = np.hstack((v1, v2))
print(data2) # [1 2 3 4 5 6]
print()
data3 = np.concatenate((v1, v2), axis=0)
print(data3)
print()