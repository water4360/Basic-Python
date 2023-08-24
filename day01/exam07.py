#230822(화)
import random

print('while문')
num = 1
while num <= 10 :
    print(num, end=' ')
    num += 1
print()

print('1~10까지 출력하기')
for i in range(10) :
    print(i+1, end=' ')
print()

print('홀수만 출력')
for i in range(10) :
    if(i+1) % 2 :
        print(i+1, end=' ')
print()

print('range 활용해서 홀수만 출력하기')
for i in range(0, 10, 2) :
    print(i+1, end=' ')
print()

print('시퀀스형 텍스트 출력하기')
names = ['김미미', '이미미', '안미미']
for name in names :
    print(name, end=' ')
print()

'''
    *
    **
    ***
    ****
    *****
'''
print('별출력하기1 * ~ *****')
for i in range(1, 6) :
    print('*' * i)
print()

'''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''
print('별출력하기2')
for i in range(0, 5) :
    if i <= 5 :
        print('*' * i)
for j in range(5, 0, -1) :
    print('*' * j)
print()

print('별출력하기2 - 교수님 해설')
for i in range(9) :
    # print('*' * (i+1)) if i < 5 else print('*' * (9-i)) # 한줄로 하면 이렇게.
    cnt = (i + 1) if i < 5 else (9 - i)
    print('*' * cnt)


########################## 출력안됨
print('369게임 - 짝, 뽀숑, 뽀뽀숑, 뽀뽀뽀숑짝')
# random_num = random.randrange(20, 51)
random_num = random.randint(20, 50)
print('랜덤정수 : ', random_num)

#최대 수까지 = i가 증가
# for i in range(random_num) :
#     num = i + 1
#     # 10으로 나눈 나머지가 3, 6, 9이면서
#     if (num % 10) % 3 == 0 :
#         # 뒷자리가 3의 배수이면
#         if num % 3 == 0 :
#             print(num, '짝')
#         else :
#             print(num, '-')
#         # 10의 배수면? 뽀숑
#         if num >= 10 and num % 10 == 0 :
#             print('뽀' * (num // 10), '숑')
#         # 10보다 큰 애의 나머지가 3의 배수면? 짝
#         # if (num%10) % 3 == 0 :
#             # 몫도 3의 배수 & 나머지도 3의 배수면? 짝짝
#     else :
#         print(num, '-')


# 뒷자리만 3,6,9... 짝
# 앞자리만 3의배수 30, 31, 32... 짝
# 앞자리도 3의배수&뒷자리도 369, 33, 36, 39 짝짝

# for i in range(1, random_num) :
#     # 뒷자리가 3, 6, 9인 숫자
#     if (i % 10) in (3, 6, 9) :
#         # 앞자리가 3의 배수인 애들
#         if (i // 10) in (3, 6, 9) :
#             print(i, '짝짝')
#         # 앞자리만 3의 배수 30, 31, 32...
#         else :
#             print(i, '짝')
#     # 10, 20, 30...
#     elif i >= 10 and i % 10 == 0 :
#         # 앞자리가 3의 배수
#         if (i // 10) in (3, 6, 9) :
#             print(i, '뽀' * (i // 10), '숑짝', sep='')
#         else :
#             print(i, '뽀' * (i // 10), '숑', sep='')
#     else :
#         print(i, '-')

for i in range(1, random_num) :
    #10, 20, 30...
    if (i % 10) == 0 :
        # 30, 60, 90...
        if (i // 10) % 3 > 0 :
            print(i, '뽀'*(i//10), '숑짝', sep='')
        # 10, 20, 40...
        else :
            print(i, '뽀'*(i//10), '숑', sep='')
    #일의 자리가 1~9번대
    else :
        #앞자리가 3의 배수
        if (i // 10 ) % 3 > 0 :
            #뒷자리가 3,6,9
            if (i % 10) % 3 > 0 :
                print(i, '짝')
            else :
                print(i, '-')
        #그 외
        elif (i % 10) % 3 == 0 :
            print(i, '짝')
        else :
            print(i, '-')
########################## 출력안됨