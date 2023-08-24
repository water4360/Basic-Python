'''
    1~10 사이의 정수 10개를 원소로 가지는 list data 선언
'''
import copy

# 방법1
# data = [1, 2.... 10 다 적어주기]

# 방법2
# data = list()
# for i in range(10) :
#     data.append(i+1)
# print(data)

# ★방법3 - list comprehension
# list = [삽입할 데이터 for i in 순환범위 if 조건]
data = [i for i in range(10) if i % 2]
print(data)
data = [2*i+1 for i in range(10) if 2*i+1 < 10]
print(data)

# 구구단은 어떻게 넣을까?
dan = 4
guguData = [dan * i for dan in range(2, 10)
                    for i in range(1, 10)]
print(guguData)

strData = ['hello', 'good', 'bye', 'welcome', 'apple', 'sorry']
fiveStrData = [s for s in strData if len(s) == 5] #5글자 이상인 데이터만 뽑아내기
print(fiveStrData)

copyStrData = strData[:]
copyStrData2 = strData.copy()
# copyStrData3 = copy.deepcopy(strData)

print('strData : ', strData, id(strData))
# 챗지피티에서는 얘네 다 shallow 카피라는데.
print('slicing-copyStrData : ', copyStrData, id(copyStrData))
print('copy()-copyStrData2 : ', copyStrData2, id(copyStrData2))
# print('deep-copyStrData3 : ', copyStrData3, id(copyStrData3))

