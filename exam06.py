#230822(화)
num = int(input('정수 입력 : '))
# 2로 나눈 나머지는 0 또는 1이라는 점,
# 0은 False, 0이 아니면 True라는 점을 고려하면
# 아래와 같이 간단하게 표현하는 것도 가능
if num > 0 :
    if num % 2 :
        print(num, ': 홀수')
    else :
        print(num, ': 짝수')
else :
    print(num, ': 올바르지 않은 숫자')

#다중if문을 쓰는 방법
if num < 0 :
    print(f'{num} : 음수')
elif num == 0 :
    print(f'{num} : 제로')
elif num % 2 :
    print(f'{num} : 홀수')
else :
    print(f'{num} : 짝수')


# import random
#
# r = int(random.random() * 10)
#
# if r % 2 == 0:
#     print(f'{r} : 짝수')
# else:
#     print(f'{r} : 홀수')