#230821(월) Day01
print('Hello Python!!')


#230822(화) Day02
'''
    정수 2개 입력받아 사칙연산 결과 출력
'''

# 자동으로 줄바꿈('\n')되게 되어있는데 안하도록(end='') 설정.
# 직전 실행 = ctrl+shift+f10
# 파이썬과 JS 유사함 ("", '' 구분없음 / type 구분이 없어 유동적으로 저장 가능)
# 마음대로 들여쓰기 허용안됨. 에러남.
print('첫번째 정수 입력 : ', end='')
num01 = int(input())
# print(type(num01))
print('두번째 정수 입력 : ', end='')
num02 = int(input())
print('num02의 타입은 ? ', type(num02))

# sep 옵션 : ':'기호를 활용해 분리.
# print(num01, num02, sep=':')
# 야매로 아래와 같이 쓸 수도 있겠지만.
print('야매 더하기 : ', num01, '+', num02, '=', num01+num02)
print('formatting(-) : %d - %d = %d' % (num01, num02, num01-num02))
print('formatting(*) : %d * %d = %d' % (num01, num02, num01*num02))
print('formatting(/) : %d / %d = %d' % (num01, num02, num01/num02))
print('(그런데...)int로 int를 나눠도 int가 안나오기도 함 : ', num01/num02)
print('formatting(%%) : %d %% %d = %d' % (num01, num02, num01%num02), end='\n\n')
print('위와 같은 포맷은 문제가 많음. 그래서 아래와 같은 {n}포맷을 씀ㅋ')
print('{0} / {1} = {2}'.format(num01,num02,num01/num02), end='\n\n')
print('근데 0,1,2... 다 적으려니 귀찮아. 그래서 아래와 같은 f포맷을 씀ㅋㅋ')
print(f'{num01} / {num02} = {num01 / num02}')
print('몫만 구하고 싶다면, 소수점을 날리기 위해 int로 형변환 하는 대신 // 두개 써주면 된다!')
print(f'{num01} / {num02} = {num01 // num02}')
print(f'{num01} % {num02} = {num01 % num02}')
print('거듭제곱을 하고 싶다면? **를 두 번 써주면 된다!')
print(f'{num01} ** {num02} = {num01 ** num02}')
print('문자를 연산에 포함시키면? 그것을 계산한다!')
print('2' * 3)
print('2' + 3)
