from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()


X = [[168, 0], [166, 0], [173, 0], [165, 0], [177, 0], [163, 0],
     [178, 0], [172, 0], [163, 1], [162, 1], [171, 1], [162, 1], [164, 1], [162, 1], [158, 1], [173, 1]]
y = [65, 61, 68, 63, 68, 61, 76, 67, 55, 51, 59, 53, 61, 56, 44, 57]

# print(len(X))
# print(len(y))

#직선이 만들어지고.
regr.fit(X, y)
#
#직선에 대한 기울기와 절편 구하기
coef = regr.coef_
intercept = regr.intercept_
score = regr.score(X, y)

print('y ={} * X + {:.2f}'.format(coef.round(2), intercept))
print('데이터와 선형 회귀 직선의 관계점수 : {:.1%}'.format(score))
print('추정몸무게', regr.predict([[167, 0], [167, 1]]))