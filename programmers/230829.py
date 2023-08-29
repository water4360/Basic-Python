# 마지막 두 원소
def solution(num_list):
    if num_list[-1] > num_list[-2] :
        num_list.append(num_list[-1] - num_list[-2])
    else :
        num_list.append(num_list[-1]*2)
    return num_list

#모범 답안
# def solution(num_list):
#     a = num_list[-1]
#     b = num_list[-2]
#     num_list.append(a - b if a > b else a * 2)
#     return num_list
# print(solution([2,1,6]))
# print(solution([5,2,1,7,5]))


#수 조작하기1
# 치환해서 한꺼번에 sum 날리면 될 것 같은데...
# def solution(n, control):
#     for w in control :
#         if w == 'w' :
#             n += 1
#         elif w == 's' :
#             n -= 1
#         elif w == 'd' :
#             n += 10
#         else :
#             n -= 10
#         # print(n)
#     return n
#
# # 모범 답안
# def solution(n, control) :
#     answer = 0
#     map = {'w':1, 's':-1, 'd':10, 'a':-10}
#     for i in control :
#         answer += map[i]
#     return answer
# print(solution(0, "wsdawsdassw"))


# 수 조작하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
# def solution(numLog):
#     answer = ''
#     for i in range(0, len(numLog)-1) :
#         n = numLog[i+1] - numLog[i]
#         if n == 1 :
#             answer += 'w'
#         elif n == -1 :
#             answer += 's'
#         elif n == 10 :
#             answer += 'd'
#         else:
#             answer += 'a'
#         # print(answer)
#     return answer
# # print(solution([0, 1, 0, 10, 0, -1, -2]))
# print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))





# 수열과 구간 쿼리 2 ***
# https://school.programmers.co.kr/learn/courses/30/lessons/181923
# def solution(arr, queries):
#     #1차 배열 찾기
#     data = []
#     for s, e, k in queries :
#         #배열 내 value 찾기 0, 4, 2
#         # s, e, k = ar[0], ar[1], ar[2] # ㅎㅎㅎ 고침!
#         #범위 내 k보다 큰 수 모음
#         nums = [i for i in arr[s:e+1] if i > k]
#
#         if nums :
#             data.append(min(nums))
#         else :
#             data.append(-1)
#         # print('data:', data)
#     return data
# arr = [0, 1, 2, 4, 3]
# que = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
# print(solution(arr, que))


# 수열과 구간 쿼리 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181924
def solution(arr, queries):
    for i, j in queries :
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    return arr

print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))










#문자열 뒤집기
# def solution(my_string):
#     return my_string[::-1]
# print(solution('jaron'))

#직각삼각형 출력하기 (별찍기)
# n = int(input('입력 : '))
# for i in range(1, n+1) :
#     print('*' * i)

# 짝수 홀수 개수
# def solution(num_list):
#     odd, even = 0, 0
#     for i in num_list :
#         if i % 2 :
#             odd += 1
#         else :
#             even += 1
#     return [even, odd]

#모범 답안 : 배열의 인덱스까지 한방에 활용
# def solution(num_list):
#     answer = [0, 0]
#     for n in num_list:
#         answer[n % 2] += 1
#     return answer
# print(solution([1, 2, 3, 4, 5]	))


# 문자 반복 출력하기
# def solution(my_string, n):
#     answer = ''
#     for w in my_string :
#         answer += (w*n)
#     return answer
# 참고 답안 : join 활용하기
# def solution(my_string, n) :
#     return ''.join(w*n for w in my_string)
# print(solution("hello", 3))