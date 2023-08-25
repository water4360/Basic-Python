#0825(금) 딕셔너리
'''
    setdefault  : 데이터 추가
    update      : key 없으면 데이터 삽입, key 있으면 데이터 수정
    pop         : 데이터 삭제
    popitem     : 마지막 데이터 삭제
    get         : key값으로 value값 반환
'''
members = {'홍길동':'01011112222', '박길동':'01033334444'}
#새로운 키&값을 추가하는 경우.
members.setdefault('윤길동', '01055556666')
#키만 추가하는 경우 none 값이 추가됨.
members.setdefault('이길동')
# 기존데이터 수정은 불가
# members.setdefault('이길동', '01077778888')
# update수정시에는 ''없이 key='value'로.
# 만약 key가 없다면 새로운 데이터를 추가함.
# 단, key=value 형태는 문자열key만 가능하므로 다른건 안될수도...!?
members.update(이길동='01077778888')
members.update(한길동='01099990000')
members.update({2023082501:'01023456789'})
members.update([[202302502, '01012341234'], ['고길동', '01056565656']])
members.update(zip(['park', '이길동'], ['8282', None]))
print('members : ', members)

value = members.pop('이길동')
print(f'pop("이길동") : {value}')

# 없는 key를 pop하면 에러가 남. 안전장치가 필요함.
value = members.pop('왕길동', '존재X')
print(f'pop("왕길동", "존재X") : {value}')
print('members.pop("이길동") : ', members)


# 마지막 아이템 삭제. 단 파이썬 3.9이상? 최신 한정.
members.popitem()
print('members.popitem() : ', members)

value = members.get('홍길동')
print(f'홍길동 연락처 : {value}')
print(f'이길동 연락처 : {members.get("이길동"), "존재X"}')