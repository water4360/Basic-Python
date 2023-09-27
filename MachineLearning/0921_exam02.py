#사이킷런 라이브러리를 사용하여 회귀 함수를 구현하는 방법

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()

X = [[163], [179], [166], [169], [171]]
y = [54, 63, 57, 56, 58]
regr.fit(X, y)

#학습데이터와 y값을 점으로 표시
plt.scatter(X, y, color='blue', marker='D')
#학습데이터를 입력으로 하여 예측값 계산
y_pred = regr.predict(X)
#계산된 기울기와 y절편을 가지는 선을 빨간색상으로 그리기.
plt.plot(X, y_pred, 'r:')

unseen = [[167]]
result = regr.predict(unseen)
print(f'동윤이의 키가{unseen}cm 이므로 몸무게는 {result.round(1)}kg으로 추정됨')

plt.show() #추가해야 파이참에서 그래프 출력가능