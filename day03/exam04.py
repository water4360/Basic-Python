# 230825(목)

members = {'홍길동':'1111-2222', '박길동':'3333-4444', '윤길동':'5555-6666'}

# 키key로만 존재여부 확인가능
print(f'홍길동 존재여부 : {"홍길동" in members}') # True
print(f'고길동 존재여부 : {"고길동" in members}') # False

print(members.keys())
print(members.values())
print(members.items())


for data in members :
    # print(data, end =' ') #이렇게 출력하면 key만 나온다.
    print(f'{data} : {members.get(data)}')
print()

# 엥? 위의 #data, end방법이랑 차이가 머지...
# 한눈에 key만 나온다는 것을 알아보는건가??
for data in members.keys() :
    print(data)
print()

for data in members.values() :
    print(data, end=' ')
print()

# key, value를 튜플 형태로 바로 뽑아낸다.
for key, value in members.items() :
    print(f'key:{key}, value:{value}')
print()

#dict.fromkeys()
print('<values는 모르지만 일단 딕셔너리를 만들고 싶을 때>')
keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys, '-')
print(mem)
