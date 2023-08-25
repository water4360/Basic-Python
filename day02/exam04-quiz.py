'''
    [어제 과제2]
    한 줄에 여러개의 데이터를 입력받음
    문자가 포함되어 잇으면 걔는 제외.
    10 5 23 89 11.2 5 16 ‘hello’ 8
    1단계 : 정수의 합 (10+5+23… 16+8)
    2단계 : 소수 출력 (5, 23, 89, 5)
    3단계 : [’’, 5, 23, 89, ‘’, 5, ‘’, ‘’, ‘’]
'''
# nums = input('숫자를 입력하세요 >> ')
# num = nums.split()
# # print(num)
# total = 0
# prime = []
# numList = []
# for i in num :
#     # i가 숫자면
#     if i.isdigit() :
#         total += int(i)
#         numList.append('')
#         cnt = []
#         for j in range(1, int(i)+1) :
#             #약수이면서
#             if int(i) % j == 0 :
#                 cnt.append(j)
#         if len(cnt) == 2 :
#             prime.append(i)
#             numList.append(i)
#     else :
#         numList.append('')
#
# print('1단계 정수의 합계 : ', total)
# print('2단계 소수 : ', prime)
# print('3단계 소수제외 : ', numList)



'''
    [과제1]
    data = [n10, n1]

    for d in data :
        if d in [3, 6, 9] :
            print~~
    이렇게 표현할 수도 있음.

    259 % 10의 나머지 9를 구하고
    259 // 10의 몫 25를 만들어서 25 % 10의 나머지 5를 구하고
    25 // 10의 몫 2를 만들어서 25 % 10의 나머지 2를 구하고
    2 // 10의 몫이 0이 나오면 반복문 중단.
'''

# # num = input('정수를 입력하세요 : ')
# num = 139
#
# #1부터 증가할 숫자
# for i in range(1, num+1) :
#     print(f'{i:<3}', end=' ')
#     #모든 숫자를 쪼개서 arr에 넣고
#     arr = []
#     while i > 0:
#         result = i % 10
#         # print('result : ', result)
#         arr.insert(0, result)
#         # print('arr : ', arr)
#         i //= 10
#         # 10으로 나눈 나머지가 0일때
#         if result % 10 == 0:
#             print('뽀', '숑', end='', sep='')
#         if result in [3, 6, 9] :
#             print('짝', end='')
#
#     print()


'''
    [과제2]
    quit 나올때까지 정수를 입력받아 각 정수의 약수를 출력
    10
    6
    36
    87
    23
    40
    quit
    10의 약수 : [1, 2, 5, 10]
    6의 약수 : [1, 2, 3, 6]
    36의 약수 : [1, 2, 3, 4, 6, 9, 12, 18, 36]
    ...
    23의 약수 : [1, 23]
    40 : 1, 2, 4, 5, 8, 10, 20, 40

    효율적으로 짜 보세요~
'''


# print('정수 입력(q 입력시 종료)')
# data = []
# while True :
#     #반복 입력
#     num = input('>> ')
#
#     #종료전&숫자라면 list에 추가
#     if num != 'q' and num.isdigit() :
#         data.append(int(num))
#     else:
#         break
#
# #i는 저장된 숫자
# for i in data :
#     print(f'{i}의 약수 : ', end='')
#     cnt = []
#     #j는 1부터 해당숫자까지.
#     for j in range(1, i+1) :
#         #나머지가 없으면 약수
#         if i % j == 0 :
#             cnt.append(j)
#             print(j, sep=' ', end=' ')
#     #1과 해당숫자만 있으면 소수
#     if len(cnt) == 2 :
#         print('(소수)', end=' ')
#     print()

print(' *** 교수님 풀이 ***')
print('정수를 입력하시오. qq 입력시 종료')
inputs = list()
while True :
    data = input()
    if data.lower() == 'qq' :
        break
    inputs.append(int(data))
print(inputs) #확인용

##아앗 여기서 comprehension을 쓰면 되는구나...
for num in inputs :
    div = [i for i in range(1, num+1) if num % (i) == 0]
    print(f'{num}의 약수 : {div}')
