# 정수 2개를 입력받아 최대 공약수 출력

# 두 수의 약수를 각각 구하고,
# 공통된 숫자를 구하고,
# 그 중에 가장 큰 숫자 max를 구하면?

# num1, num2 = map(int, input('정수를 2개 입력하세요 >> ').split())
# nums = [num1, num2]
#
# divs = []
# for num in nums :
#     div = [i for i in range(1, num+1) if num % i == 0]
#     divs.append(div)
#     print(f'"{num}"의 약수 : {div}')
#
# max_common_divisor = max(set(divs[0]) & set(divs[1]))
# print('최대 공약수 : ', max_common_divisor)


num, num2 = map(int, input('정수를 2개 입력하세요 >> ').split())
print(num, num2)

# divNum = [i for i in range(1, num+1) if num % i == 0]
divNum = set([i for i in range(1, num+1) if num % i == 0]) #이렇게 바로 묶어주는 것도 가능!
divNum2 = [i for i in range(1, num2+1) if num2 % i == 0]

#divNum2에 있는 숫자만 저장. set 함수 안쓰고도 되네
divisor = [n for n in divNum if n in divNum2]
print(f'{num} 약수들의 집합 : {divNum}')
print(f'{num2} 약수들의 집합 : {divNum2}')
print(divisor)
print(f'최대공약수 : {max(divisor)}')
print(f'최대공약수 : {max(divNum & set(divNum2))}')




# for i in nums :
#     print(f'{i}의 약수 : ', end='')
#     for j in range(1, i+1) :
#         if i % j == 0 :
#             dividor.append(j)
#             print(j, sep=' ', end=' ')
#     print()




