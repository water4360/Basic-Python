#230825(금)
# array = [9, -1, 0]
# def solution(array):
#     answer = 0
#     return answer
# sortedArray = sorted(array)
# print(sortedArray)



#230825(금) 집에서
# print('Hello Python!!')


#최빈값 구하기 ***
# 단일 개수 = 해당 값(value), 여러개 중복 = -1
# array = [1,2,3,3,3,4] #3
# array = [1,1,2,2] #-1
# 첫번째 고민
# 배열을 i로 돌면서 딕셔너리(num : cnt)로 넣는데,
# 없으면 넣고, 아니면 있는 애의 cnt를 +1

# 두번째 답
# Counter로 array 내의 수를 num과 cnt로 세고, 최빈값이랑 같은 것만 배열에 넣어서
# 길이가 1이면 단일이니 그 값을, 1보다 크면 여러개니 -1을 리턴하도록.

# from collections import Counter
# def solution(array) :
#     counter = Counter(array)
#     max_count = max(counter.values())
#     answer = [num for num, cnt in counter.items() if cnt == max_count]
#     print('answer : ', answer)
#     return answer[0] if len(answer) == 1 else -1
# print(solution([1,2,3,3,3,4]))
# print(solution([1,1,2,2,4,4]))


#짝수는 싫어요
#
# def solution(n):
#     answer = [i for i in range(1,n) if i%2]
#     return answer
# print(solution(10))



#문자열 섞기
# def solution(str1, str2):
#     answer = ''
#     for i in range(len(str1)) :
#         answer = answer + str1[i] + str2[i]
#     return answer
#
# print(solution('aaaaa', 'bbbbb'))


#문자 리스트를 문자열로 변환하기
# def solution(arr):
#     return ''.join(arr)
#
# print(solution(["a","b","c"]))

#문자열 곱하기
# def solution(my_string, k):
#     return my_string * k

#더 크게 합치기
# def solution(a, b):
#     a, b = str(a), str(b)
#     return max(int(a+b), int(b+a))
#
# print(solution(100, 3))


#두 수의 연산값 비교하기
# def solution(a, b):
#     c = 2 * a * b
#     a, b = str(a), str(b)
#     return max(int(a+b), c)
#
# print(solution(91,2))


#홀짝에 따라 다른 값 반환하기
# def solution(n) :
#     #홀수라면
#     if n % 2 :
#         odds = [i for i in range(1, n+1, 2)]
#         return sum(odds)
#     #짝수라면
#     else :
#         evens = [i * i for i in range(2, n+1, 2)]
#         return sum(evens)
# print(solution(7))
# print(solution(10))


#flag에 따라 다른 값 반환하기 ???
# def solution(a, b, flag):
#     return a + b if flag else a - b
# print(solution(-4, 7, bool('false')))
# flag에 들어오는 게 단순히 true, false인데 어떻게 조건문에 적용이 되지...?




#피자 나눠 먹기(1)
# def solution(n) :
#     piece = n // 7
#     extra = n % 7
#     #8 : 모자라는 경우
#     if piece and extra :
#         return piece+1
#     #7 : 딱떨어지는 경우
#     elif piece :
#         return piece
#     #1
#     else :
#         # print(f'piece : {piece}, extra : {extra}')
#         return 1
# 모범답안 ㅎㄷㄷ
# def solution(n):
#     return (n - 1) // 7 + 1
# print(solution(1))

#피자 나눠 먹기(2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 6명 6조각 1판 = 6
#10명 6조각 5판 = 30
# 4명 6조각 2판 = 12
# 8명 6조각 4판 = 24
#11명 6조각 3판 = 66

# n % 6 == 0이면 몫 그대로.
# 아니면 n과 6의 최대공약수로 나눈 값(=조각)을 6으로 나눈 값(=판)
# import math
# def solution(n):
#     #불필요하네1 if n % 6 :
#         return n * 6 // math.gcd(n, 6) // 6
#     #불필요하네2 return n // 6
#
# print(solution(11))

# 피자 나눠 먹기(3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816
# def solution(slice, n):
#     return (n // slice)+1 if n % slice else n // slice

#역시나 모범답안...
# def solution(slice, n):
#     return (n - 1) // slice+1
#
# print(solution(6, 12))


# 조건 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181934
def solution(ineq, eq, n,m) :
    if (ineq==">" and eq=="=") :
        return 1 if n >= m else 0
    elif (ineq=="<" and eq=="=") :
        return 1 if n <= m else 0
    elif (ineq==">" and eq=="!") :
        return 1 if n > m else 0
    else :
        return 1 if n < m else 0
print(solution("<","=",20,50))
