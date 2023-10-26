from sklearn.metrics import confusion_matrix

#01.
y_true = [1,0,1,1,0,1]
y_pred = [0,0,1,1,0,1]
confusion_matrix(y_true, y_pred)

#02.
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
# (tn,fp,fn,tp)
print((tn,fp,fn,tp)) #output (2,0,1,3)



#03. 정확도 구하기
import numpy as np
from sklearn.metrics import accuracy_score

y_pred = np.array([0,1,1,0])
y_true = np.array([0,1,0,0])
print(sum(y_true == y_pred) / len(y_true))


#04.
print('정확도', accuracy_score(y_true, y_pred))


from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

y_pred = np.array([0,1,1,0,1,1,1,0])
y_true = np.array([0,1,0,0,0,0,1,1])

print('정밀도', precision_score(y_true, y_pred))
print('민감도', recall_score(y_true, y_pred))
print('F1스코어', f1_score(y_true, y_pred))