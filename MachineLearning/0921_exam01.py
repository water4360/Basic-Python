#간단한 선형회귀를 수행해보자
import numpy as np
import time

arr_a = np.random.rand(1000000000)
arr_b = np.random.rand(1000000000)
result = np.zeros(1000000000)

#벡터화 연산
start = time.time()
result = arr_a * arr_b
end = time.time()
diff = end-start
print('벡터연산 소요시간 : ', diff)


#스칼라 연산
start2 = time.time()
for i in range(len(arr_a)):
    result[i] = arr_a[i] * arr_b[i]
end2 = time.time()
diff2 = end2-start2
print('스칼라연산 소요시간 : ', diff2)
print('10억일 때 스칼라연산과 벡터 차이 : ', diff2/diff)
