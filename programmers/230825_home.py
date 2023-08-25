#230825(금) 집에서
# print('Hello Python!!')

#최빈값 구하기 ***
# array = [1,2,3,3,3,4] #3
# array = [1,1,2,2] #-1

def solution(array) :
    answer = 0
    return answer


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