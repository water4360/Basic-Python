data = [10, 20, 30, 40]
print('data의 타입은 ? : ', type(data), ', 내용은 ? :', data)

data = list()
print('data의 타입은 ? : ', type(data), ', 내용은 ? :', data)

data = (10, 20, 30)
print('data의 타입은 ? : ', type(data), ', 내용은 ? :', data)

data = tuple()
print('data의 타입은 ? : ', type(data), ', 내용은 ? :', data)

#이 경우, int 타입의 10이 되지만
data = 10
print(type(data), data)

#이 경우, (10, 20)의 튜플로 자동 인식함.
data = 10, 20
print(type(data), data)

#range 10이라면, 0~9까지 10개의 숫자를 생성함.
data = range(10)
print(type(data), data)
print('range data를 list에 넣어보면?')
data = list(data)
print(data)

# range(시작값, 종료값, 증가값) 설정가능
# 증가값은 기본 1. 단 종료, 증가만 쓸 수는 없음. 헷갈릴테니까?

print('range(5, 15)일때')
data = list(range(5, 15))
print(data)

print('range(1, 10, 2)일때')
data = list(range(1, 10, 2))
print(data)

print('range(20, 4, -3)일때')
data = list(range(20, 4, -3))
print(data)
# 조건을 걸어서 bool 값을 얻는 것도 가능!
print('16이 data에 있니, 17이 data에 있니')
print(16 in data, 17 in data)
print('elo' in 'Hello')
print(10 in range(10))