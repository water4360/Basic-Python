#2438 - 별찍기 - 1
# n = int(input())
# for i in range(n):
#     print('*'*(i+1))
import sys

#2439 - 별찍기 - 2
# n = int(input())
# for i in range(n):
#     print((' '*(n-(i+1)))+('*'*(i+1)))

#10952 - A+B - 5
# while 1:
#     a, b = map(int, sys.stdin.readline().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

#10951 - A+B - 4
# import sys
# while 1:
#     try:
#         a, b = map(int, sys.stdin.readline().split())
#         print(a + b)
#     except:
#         break


#10807 - 개수 세기
from collections import Counter
# n = int(input())
# nums = list(map(int, input().split()))
# cnt = nums.count(int(input()))
#
# print(cnt)

#10871 - X보다 작은 수
# n, x = map(int, input().split())
# nums = list(map(int, input().split()))
# result = [i for i in nums if x > i]
# print(*result)

#10818 - 최소, 최대
# n = int(input())
# nums = list(map(int, input().split()))
# print(min(nums), max(nums))

#2562 - 최댓값
# nums = [int(input()) for i in range(9)]
# print(max(nums))
# print(nums.index(max(nums))+1)

#10810 - 공 넣기
#n은 공번호. m은 횟수.
# import sys
# n, m = map(int, sys.stdin.readline().split())
# basket = [0]*n
# print('처음:', basket)
# for cnt in range(m):
#     i, j, k = map(int, sys.stdin.readline().split())
#     for x in range(i-1, j):
#         basket[x] = k
#     print('중간:', basket)
# print(*basket)


#10813 - 공 바꾸기
# import sys
# n, m = map(int, sys.stdin.readline().split())
# basket = [n for n in range(1, n+1)]
# # print('초기',basket)
# for cnt in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
# print(*basket)
#참고답안 - open(0).read()로 사용자 입력.
# map(int, open(0).read().split())

#5597번 - 과제 안 내신 분..?
# import sys
#
# std = [0]*30
# # print(std)
#
# for i in range(28):
#     no = int(sys.stdin.readline())
#     std[no-1] = no
#
# for n in std:
#     if n == 0:
#         print(std.index(n)+1)
#         std[std.index(n)] = std.index(n)+1
# print(std)
#참고 답안 : 번호 리스트에서 제출한 번호를 삭제하는 방법.
# std = [i for i in range(1,31)]
# print(std)
# for i in range(28):
#     std.remove(int(input()))
# print(min(std))
# print(max(std))

#3052 - 나머지
# nums = {int(input())%42 for i in range(10)}
# print(len(nums))

#10811 - 바구니 뒤집기 / input과 인덱스를 자꾸 헷갈리네요.
# n, m = map(int, input().split())
# basket = [n+1 for n in range(n)]
# # print(basket)
# for o in range(m):
#     i, j = map(int, input().split())
#     basket[i-1:j] = reversed(basket[i-1:j])
#     # print(basket)
# print(*basket)

#1546 - 평균(세준이의 조작)
n = int(input())
score = list(map(int, input().split()))
m = max(score)
avg = 0
for s in score:
    avg += s/m*100
print(avg/n)