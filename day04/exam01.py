# 230828(월)
# day04/exam07-quiz.py에 이어서
# set의 데이터 유형
# union(합집합), intersection(교집합)
# difference(차집합) = 합집합 - 교집합
# symmetric_difference(대칭차집합) = 서로 안겹치는 것.

data = set([1,2,3,4])
data2 = {1,4,5,6}
print(type(data), data)
print(type(data2), data2)
print(f'합집합 data.union(data2) : {data.union(data2)}')
print(f'합집합 data | data2 : {data | data2}')
print(f'교집합 data.intersection(data2) : {data.intersection(data2)}')
print(f'교집합 data & data) : {data & data}')
print(f'차집합=합집합-교집합 data.difference(data2) : {data.difference(data2)}')
print(f'차집합 data - data2) : {data - data2}')
print(f'대칭차집합 data.symmetric_difference(data2) : {data.symmetric_difference(data2)}')
print(f'대칭차집합 data ^ data2 : {data ^ data2}')
print()
print('원본 데이터는 변하지 않음 ', data, data2)
