import numpy as np

X = np.array([1, 4.5, 9, 10, 13])
y = np.array([0, 0.2, 2.5, 5.4, 7.3])

#w, b의 초기값을 0으로.
w, b = 0, 0
#학습률과 학습횟수
learning_rate, epoch  = 0.005, 1000
n = len(X)

for i in range(epoch):  #epoch만큼 반복학습
    y_pred = w*X + b    #w, b를 이용한 작업T
    error = y_pred - y  #성능척도 P
    w = w - learning_rate * (error * X).sum() #경험 E로 개선
    b = b - learning_rate * error.sum()

print(f'w = {w.round(2)}, b = {b.round(2)}')