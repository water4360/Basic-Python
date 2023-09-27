from sklearn import linear_model
import matplotlib.pyplot as plt

regr = linear_model.LinearRegression()
regr_f = linear_model.LinearRegression()

# X = [[168], [166], [173], [165], [177], [163], [178], [172], [163], [162], [171], [162], [164], [162], [158], [173]]
# y = [65, 61, 68, 63, 68, 61, 76, 67, 55, 51, 59, 53, 61, 56, 44, 57]

X1 = [[168], [166], [173], [165], [177], [163], [178], [172]]
y1 = [65, 61, 68, 63, 68, 61, 76, 67]

X2 = [[163], [162], [171], [162], [164], [162], [158], [173]]
y2 = [55, 51, 59, 53, 61, 56, 44, 57]


# print(len(X))
# print(len(y))
#직선이 만들어지고.
regr.fit(X1, y1)
regr_f.fit(X2, y2)

#직선에 대한 기울기와 절편 구하기
coef = regr.coef_
coef_f = regr_f.coef_
intercept = regr.intercept_
intercept_f = regr_f.intercept_
# score = regr.score(X, y)
score = regr.score(X1, y1)
score_f = regr_f.score(X2, y2)

print('y ={} * X + {:.2f}'.format(coef.round(2), intercept))
print('데이터와 선형 회귀 직선의 관계점수 : {:.1%}'.format(score))

plt.scatter(X1, y1, color='blue', marker='D')
plt.scatter(X2, y2, color='red', marker='D')
y1_pred = regr.predict(X1)
y2_pred = regr_f.predict(X2)
plt.plot(X1, y1_pred, 'k:')
plt.plot(X2, y2_pred, 'k:')
plt.show()
