#230828(월)

data = set()
print(f'{data} 원소의 개수 : {len(data)}')
for i in range(10) :
    data.add(i+1)

data.add(5) # 중복허용X
data.add('5') #다른 자료형은 가능
print(f'원본 {data} 원소의 개수 : {len(data)}')
data.remove('5')
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')

# 없는거 또 지우려고 하면 에러남. 그래서 사전에 있는지 확인하는 조건이 필요함.
# data.remove('5')
# 단, discard는 에러가 나지 않음. 하지만 에러가 필요한 경우도 있으므로 적절하게 쓰는 것이 좋음.
data.discard(5)
print(f'remove(5) 후 {data} 원소의 개수 : {len(data)}')
print()

# copy = data #얕은 복사
copy = data.copy() #깊은 복사
print(f'이전 data : {data}')
print(f'이전 copy : {copy}')
copy.add(5)
print(f'이후 data : {data}')
print(f'이후 copy : {copy}')
print('얕은 복사때는 data, copy 상호변경, 깊은 복사때는 건드린 데이터도 변경')

# divisor = [n for n in divNum if n in divNum2]


