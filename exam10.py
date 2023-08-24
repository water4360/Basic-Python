'''
    무작위 정수 입력받고
    1. 정수의 합(문자 무시)
    2. 소수만 출력

'''


data = input('데이터를 입력하세요 : ').split()
print(type(data), data)

for numStr in data :
    if numStr.isdigit() :  #숫자인지 확인하는 내장함수.
        num = int(numStr) #int로 변환해줘야 소수여부를 판단할 수 있지.
    # for i in range(2, num) :
    #     if num % i == 0 : #자기자신으로 나눴을때 0인 것만.
    #         cnt = cnt + 1


num = int(data[0])
i = 2
while i < num and num % i :
    i += 1
print('소수' if i == num else '소수아님')