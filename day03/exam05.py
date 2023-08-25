# 230825(금)
# 패스워드 변경 서비스

members = {'aaa':'1111', 'bbb':'2222', 'ccc':'3333', 'ddd':'4444'}


print('*** 패스워드 변경서비스 ***')
id = input('아이디를 입력하세요 : ')

# 또는 있는 경우, pass를 할 수도.
# if id in members :
#     pass

if id not in members :
    print(f'입력하신 아이디({id})는 존재하지 않아요 :(')
    print('패스워드 변경서비스를 종료할게요')
    exit(0)
else :
    pw = input('현재 패스워드를 입력해주세요 : ')
    if members.get(id) != pw :
        print('패스워드가 일치하지 않아요')
        print('패스워드 변경서비스를 종료할게요')
        exit(0)
    else :
        newPw = input('변경할 패스워드를 입력해주세요 : ')
        # members.update(id=newPw) #id자체가 변수가 아닌 상수로 인식되어버림
        # members.update([[id, newPw]]) #리스트 형태
        # members.update({id:newPw}) #또는 딕셔너리 형태로
        members[id] = newPw

print('<전체 회원 목록>')
print('아이디\t패스워드')
for id, pw in members.items() :
    print(f'{id:<6}\t{pw}')
print()