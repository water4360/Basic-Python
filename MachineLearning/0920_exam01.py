
#예제1
# sum = 0
# for i in [1,2,3,4,5]:
#     print(i, "를 더하는 중")
#     sum += i
# print("합계 = ", sum)


#예제2
# for i in range(5, 10):
#     print("i = ", i)
# print()
#
# for i in range(1, 10, 3):
#     print("i = ", i)
# print()
#
# for i in range(10, 7, -1):
#     print("i = ", i)



#예제3
# import time
#
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print('발사!')


#예제4
# response = "아니"
# while response == "아니":
#     response = input("엄마, 저녁 다 됐어? ")
# print("먹자!")


#예제5
# password = "1234"
# userInput = ""
# while userInput != password:
#     userInput = input('암호를 입력하시오 : ')
# print('로그인 성공!')


#예제6
# count = 1
# sum = 0
# while count <= 10:
#     sum += count
#     count += 1
# print('합계 =', sum)


#예제7
# while True:
#     light = input('신호등 색상을 입력하세요(예:초록, 빨강) :')
#     if light == '초록':
#         break
#     else:
#         print('wait...')
# print('이제 출발하세요!')

#예제8
from sklearn import datasets

d=datasets.load_iris()
print(d.DESCR)

for i in range(0, len(d.data)):
    print(i+1, d.data[i], d.target[i])