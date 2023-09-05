
#2884 - 알람 시계
# 분만 바뀔때
# 시와 분이 바뀔때
# h, m = map(int, input().split())
# #11:45
# if m >= 45:
#     print(h, m-45)
# #10:10
# else:
#     if 0 < h & h <= 23:
#         print(h-1, m+15)
#     else:
#         print(23, m+15)


#2525 - 오븐 시계
# h, m = map(int, input().split())
# time = int(input())
#
# h += (m+time)//60
# m = (m+time)%60
#
# if 0 <= h & h <= 23:
#     print(h, m)
# else:
#     print(h-24, m)

#2480 - 주사위 세개
# 같은눈 3개 10,000원+(같은 눈)×1,000원
# 같은눈 2개 1,000원+(같은 눈)×100원
#  (그 중 가장 큰 눈)×100원
# a, b, c = map(int, input().split())
# list = sorted([a, b, c])
#
# if len(set(list)) == 1:
#     print(10000+a*1000)
# elif len(set(list)) == 2:
#     print(1000+list[1]*100)
# else:
#     print(max(list)*100)


#2739 - 구구단
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')


#10950번 - A+B - 3
# cnt = int(input())
# for i in range(cnt):
#     a, b = map(int, input().split())
#     print(a+b)

#8393 - 합
# n = int(input())
# for i in range(n):
#     n += i
# n = int(input())
# print(n*-~n//2)

#25304 - 영수증
# x, n = int(input()), int(input())
# total = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     total += a * b
# print('Yes' if total == x else 'No')

#25314 - 코딩은 체육과목 입니다
# n = int(input())
# print(f"{'long '*(n//4)}int")


#15552 - 빠른A+B
# import sys
# t = int(sys.stdin.readline().strip())
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().strip().split())
#     print(a + b)


#11021 - A+B - 7
# import sys
# t = int(sys.stdin.readline())
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f'Case #{i+1}: {a+b}')

#11022 - A+B - 8
import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {a} + {b} = {a+b}')