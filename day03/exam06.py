# 230825(금)
# 딕셔너리도 comprehension 가능하지 않을까~~?

keys = ['name', 'age', 'addr']

# members = {key:value for  in   }
#{key:value로 넣기. key,value로 뽑기. keys로 키를 삼은 dict에서 모든 아이템을}
# members = {key:value for key, value in dict.fromkeys(keys).items()}

members = {'홍길동':'32거2345', '고길동':'26소2756', '윤길동':'89나2134'}

# key:value의 위치만 변경해서 이렇게 value로 key를 뽑아내는 것도 가능!!
owner = {carNo:name for name, carNo in members.items()}
print('차주 : ', owner.get('26소2756'))
print('차주 : ', {name for name, carNo in members.items() if carNo=='26소2756'})

data = [name for name, carNo in members.items()
        if carNo=='26소2756']
print('data : ', data)
print('data[0] : ', data[0])

# 홍길동의 차량번호 검색 easy
print(members.get('홍길동'))

# 차량번호 26소2756 차주 검색
# for key, value in members.items() :
#     if value == '26소2756' :
#         print(key)
#         break
