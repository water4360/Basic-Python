# 230902(토)

# 점의 위치 구하기
# def solution(dot):
#     if dot[0] > 0 :
#         if dot[1] > 0 :
#             return 1
#         else :
#             return 4
#     else :
#         if dot[1] > 0 :
#             return 2
#         else :
#             return 3
#
# print(solution([2,4]))


#2차원으로 만들기
# 0: 3 3: 6
# def solution(num_list, n):
#     answer = []
#     for i in range(len(num_list)//n) :
#         answer.append(num_list[i*n:(i*n)+n])
#     return answer
#모범 답안, range를 갖고오고도 스텝을 못 썼네ㅋㅋ
# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n) :
#         answer.append(num_list[i:i+n])
#     return answer
# print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
# print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))

#공 던지기 **
# def solution(numbers, k):
#     answer = 0
#     for n in range(len(numbers)) :
#         print(n+2)
#     return answer
#
# print(solution([1,2,3,4,5,6], 5))


#배열 회전시키기
# def solution(numbers, direction):
#     if direction=="right" :
#         numbers.insert(0, numbers.pop(-1))
#     else :
#         numbers.append(numbers.pop(0))
#     return numbers
#
#
# print(solution([1, 2, 3], "right"))
# print(solution([4, 455, 6, 4, -1, 45, 6], "left"))

#문자열의 앞의 n글자
# def solution(my_string, n):
#     return my_string[:n]
#
# print(solution("ProgrammerS123", 11))

#접두사인지 확인하기
# def solution(my_string, is_prefix):
#     return 1 if my_string[:len(is_prefix)] == is_prefix else 0
# 참고 : 내장함수 startswith를 사용하기
# def solution(my_string, is_prefix):
#     return 1 if my_string.startswith(is_prefix, 0, len(is_prefix)) else 0
#
# print(solution("banana","ban"))

# 문자열 뒤집기
# reversed는 항상 받아줄 배열이 필요하구나.
# def solution(my_string, s, e):
#     # part = [w for w in my_string]
#     # part[s:e+1] = reversed(my_string[s:e+1])
#     # return ''.join(part[:s]+part[s:e+1]+part[e+1:])
#     return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:] # 모범답안
#
# print(solution("Progra21Sremm3",6,12))
# print(solution("Stanley1yelnatS",4,10))


# 세로 읽기
def solution(my_string, m, c):
    for w in range(len(my_string)//m) :
        print(my_string[w * m])
    return ''

print(solution("ihrhbakrfpndopljhygc",4,2))
print(solution("programmers",1,1))