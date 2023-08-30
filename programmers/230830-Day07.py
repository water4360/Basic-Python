# 특정 문자 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# def solution(my_string, letter):
#     my_string = ''.join(c for c in my_string if c not in letter)
#     return my_string
# # 참고답안 - replace 활용!
# def solution(my_string, letter) :
#     return my_string.replace(letter, '')
# print(solution("abcdef", "f"))
# print(solution("BCBdbe", "B"))


# 각도기
# def solution(angle):
#     if angle == 180 :
#         return 4
#     elif angle < 180 and angle > 90:
#         return 3
#     elif angle == 90 :
#         return 2
#     else :
#         return 1
# print(solution(70))

# 양꼬치
# def solution(n, k):
#     o = 12000 * n
#     answer = o + 2000 * k - 2000 * (o // 10)
#     return answer
# def solution(n, k):
#     # o = 12000 * n #양꼬치 원래값
#     # s = 2000 * k #음료수값
#     # return (12000 * n) + (2000 * (k - n // 10)) # 모범답안
#     return (12000 * n) + (2000 * k) - (2000 * (n // 10))
#
# print(solution(10, 3))
# print(solution(64, 6))

# 짝수의 합
# def solution(n):
#     answer = [i for i in range(n+1) if not i % 2]
#     return sum(answer)
# 모범 답안. iterable 객체(range)를 바로 활용. if 없이 풀기
# def solution(n):
#     return sum([i for i in range(2, n+1, 2)])
#
# print(solution(10))




# 수열과 구간 쿼리 4
# https://school.programmers.co.kr/learn/courses/30/lessons/181922
# def solution(arr, queries):
#     #041, 032, 033. 3번을 돌면서
#     for s, e, k in queries :
#         print('sek', s,e,k)
#         for i in range(s, e+1) :
#         # for i in arr :
#             if i % k == 0 :
#                 print(f'{s}보다 크거나 같고 {e}보다 작거나 같은 {i}')
#                 arr[i] += 1
#         print(arr)
#     return arr
# print(solution([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]]))

# 배열 만들기 2
# def solution(l, r):
#     answer = []
#     return answer


# 카운트 업
# 10초각 생략


# 콜라츠 수열 만들기
# def solution(n):
#     answer = []
#     while True :
#         answer.append(n)
#         n = n // 2 if not n % 2 else 3 * n + 1
#         # print(f'{cnt} : {n}')
#         if n == 1 :
#             answer.append(n)
#             break
#     return answer
# print(solution(10))



# 배열 만들기 4 **
# def solution(arr):
#     i = 0
#     stk = []
#     while i < len(arr) :
#         if len(stk) == 0 or stk[-1] < arr[i] :
#             stk.append(arr[i])
#             i += 1
#             # print(f'{i} : ', stk)
#         else :
#             stk.pop(-1)
#     return stk
# print(solution([1, 4, 2, 5, 3]))





# 배열 만들기 2
# 5, 55, 555, 50, 550, 500, 505
# 10으로 나눈 몫이 5, 몫이 10의 배수이며 나머지가 5...
# 5 * 1,10,11,111,110,100,101
# def solution(l, r):
#     answer = []
#     n = 1
#     while True :
#         #1~... 이진수에 5를 곱하기.
#         num = 5 * int(bin(n)[2:])
#         # print(f'{n}:{num}')
#         if num >= l and num <= r :
#             answer.append(num)
#         if num >= r :
#             #배열이 비어있으면 -1
#             if not answer :
#                 answer.append(-1)
#                 break
#             break
#         n += 1
#     return answer
def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if not set(str(num)) - set(['0', '5']):
            answer.append(num)
    return answer if answer else [-1]

print(solution(5, 505))


