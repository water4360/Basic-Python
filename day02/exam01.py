#230823(수)
'''
    list 내장함수
    append  : 데이터추가(마지막)
    insert  : 데이터추가(지정 가능)
    pop     : 데이터 삭제(마지막)[v]
    remove  : 데이터 삭제(지정 가능)[v]
    index   : 특정값 위치 검색
    count   : 특정값 빈도수(총 몇 개?)
    reverse : 역정렬
    sort    : 정렬 (임시정렬 sorted(data), 원본적용 data.sort() 구분할 것)
    clear   : 리스트 요소 전부 삭제[v]
'''
data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print('데이터 확인용')
print(data, id(data))
#stack(LIFO)처럼 쓰려면
delData = data.pop()
print('삭제된 값 : ', delData)
print('10,20,30이 차례대로 들어가고 30이 삭제됨\n')

#Queue(FIFO)처럼 쓰려면
data = list()
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)
print('10,20,30이 차례대로 들어가고 10이 삭제됨\n')

#물론 pop을 이용해서 queue처럼? 쓸 수도 있음
data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop(1) #근데 pop도 인덱스를 사용할 수 있음.
print('삭제된 값 : ', delData)
print('10,20,30이 차례대로 들어가고 지정한 1번째 값, 20이 삭제됨\n')

data = [10, 20, 30, 40, 30]
idx = data.index(30)
cnt = data.count(30)
print('위치 : ', idx) #처음 발견된 데이터 위치
print('개수 : ', cnt) #총 개수
print('before : ', data)
data.remove(30) #처음 발견된 데이터 삭제
print('after : ', data)
print()

print('list에 있는 데이터 하나씩 출력하기')
print('방법1')
for i in range(len(data)) :
    print(data[i], end=' ') #결과 : 10 20 40 30
print()
print('방법2 - 향상된 for문st?')
for d in data :
    print(d, end=' ') #결과 : 10 20 40 30
print()
print('방법3 - iterator순환자')
for d in iter(data) :
    print(d, end=' ') #결과 : 10 20 40 30
print()
# 이건 그냥 혼자 해본것
# ite = iter(data)
# while ite :
#   print(next(ite))


'''
    결과
    [0] : 10
    [1] : 20
    [2] : 40
    [3] : 30
    그런데 enumerate 안에
    start를 1로 지정하면 index도 [1]부터 시작
    start를 100으로 지정하면 [100]부터 시작
'''
print('enumerate와 2개의 변수로 표기하기')
for index, d in enumerate(data, start=13) :
    print(f'[{index}] : {d}')



print('역순으로 데이터 출력하기!')
print('방법1 - data reverse역전')
data.reverse()
for d in iter(data) :
    print(d, end=' ') # 결과 : 30 40 20 10
print()
data.reverse()

# data2 = reversed(data)
# print('data : ', data)
# print('data2 : ', next(data2))

print('방법2 - reverse두 번 안쓰는 효율적인 방법')
for d in reversed(data) :
    print(d, end=' ') #결과 : 30 40 20 10
print()

# data.sort() #원본 데이터를 건드려서 오름차순 정렬
# print(data)

print(sorted(data)) #임시 정렬 [10, 20, 30, 40] / reversed=False(기본값:오름차순), True(내림차순)
print(data) #그래서 원본 데이터가 변경되지 않음. [10, 20, 40, 30]
print(sorted(data, reverse=True)) #내림차순 정렬 [40, 30, 20, 10]

data = [10, 20]
# for i in range(len(data)) :
    # data.pop(0) #0번지 data계속 지우도록. 결과 - 빈배열[]
# data.clear() #통째로 지우기 방법1
del data[:] #통째로 지우기 방법2
print(data)

data = [10, 20, 30, 40]
print('list에 있는 데이터 -값으로 역순출력하기')
for i in range(1, len(data)+1) :
    print(data[-i], end=' ') #결과 : 10 20 40 30
print()

