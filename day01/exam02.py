# 230822(화)
# num01 = input('첫번째 정수 입력 : ')
# num02 = input('두번째 정수 입력 : ')
# print(num01, num02)


#한 번에 입력받은 2개의 값을 각각 할당하고 싶다면?
# map(int, ['12', '5'])
# print(type('12, 5'.split()))
num01, num02 = map(int, input('두 개의 정수를 입력 : ').split())
print(type(num01), type(num02))