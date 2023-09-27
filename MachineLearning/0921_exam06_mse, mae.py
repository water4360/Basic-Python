import numpy as np
from sklearn.metrics import mean_squared_error

y = np.array([1.2, 2.4, 2.5, 4.6, 5.4])
y_hat = np.array([1, 2, 3, 4, 5])
# y_hat과 y의 차이값의 제곱
diff = (y_hat - y) ** 2

e_mse = diff.sum() / len(y)
print('평균 제곱 오차mse      =', e_mse)
print('사이킷런으로 구하는 mse =', mean_squared_error(y_hat, y))
print()


a = np.array([0.9, 1.3, 3.3, 3.8])
b = np.array([0.5, 1.9, 3.4, 4.4])
model_true = np.array([1, 2, 3, 4])

diff = (a - b) ** 2
a_mae = sum(abs(a-model_true)) / len(model_true)
b_mae = sum(abs(b-model_true)) / len(model_true)
print('A의 평균절대오차mae =', a_mae)
print('B의 평균절대오차mae =', b_mae)

a_mse = sum((a - model_true)**2) / len(model_true)
b_mse = sum((b - model_true)**2) / len(model_true)
print('A의 평균제곱오차mse =', a_mse)
print('B의 평균제곱오차mse =', b_mse)
