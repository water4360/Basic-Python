# def solution(num_list):
#     answer = 0
#     return answer

# 원소들의 곱과 합
# def solution(num_list):
#     result1 = 1
#     result2 = 0
#     for i in num_list :
#         result1 *= i
#     result2 = sum(num_list)*sum(num_list)
#     print('곱 : ', result1)
#     print('합의 제곱 : ', result2)
#     return 1 if result1 < result2 else 0
# print(solution([3,4,5,2,1]))


#이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
# def solution(num_list):
#     oddstr = ''
#     evenstr = ''
#     for i in num_list :
#         if i % 2 :
#             oddstr += str(i)
#         else :
#             evenstr += str(i)
#     return int(oddstr)+int(evenstr)
# print(solution([3, 4, 5, 2, 1]))


# 주사위 게임 2
# def solution(a, b, c):
#     if a != b and b != c and a != c : #다 다를때
#         return a+b+c
#     elif a == b and b == c : #다 같을때
#         return (a*3) * (a**2*3) * (a**3*3)
#     else : #두개만 같을때
#         return (a+b+c) * (a**2 + b**2 + c**2)
# 모 범 답 안! set으로 중복값 구하는 것!
# def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)
# print(solution(5,3,3))

#코드 처리하기
# def solution(code):
#     mode = 0
#     ret = ''
#     for i in range(len(code)):
#         #mode가 0일때
#         if mode == 0 :
#             #idx가 "1"이 아니고 i가 짝수일때
#             if code[i] != "1" and i % 2 == 0 :
#                 ret += code[i]
#             elif code[i] == "1" :
#                 mode = 1
#         #mode가 1일때
#         else :
#             if code[i] != "1" and i % 2 :
#                 ret += code[i]
#             elif code[i] == "1" :
#                 mode = 0
#     return ret if len(ret) else "EMPTY"
# print(solution("abc1abc1abc"))


#등차수열의 특정한 항만 더하기
# 딕셔너리처럼 2중 배열을 해서 만들어야하려나.[i][true]인것?
# def solution(a, d, included):
#     answer = 0
#     for tf in included :
#         if tf :
#             answer += a #True일때만 합치기
#         a += d # 꼬박꼬박 4씩 증가
#         # print('a : ', a)
#         # print('answer : ', answer)
#     return answer
#
# print(solution(3, 4, [True, False, False, True, True]))


#옷가게 할인 받기
def solution(price):
    if price >= 500000 :
        price = price * 0.8
    elif price >= 300000 :
        price = price * 0.9
    elif price >= 100000 :
        price = price * 0.95
    return int(price)

# 튜플을 이용한 모범답안
# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():
#         if price >= discount_price:
#             return int(price * discount_rate)
# print(solution(150000))



#아이스 아메리카노
# def solution(money):
#     return [money // 5500, money % 5500]
#
# print(solution(11000))


#배열 뒤집기
def solution(num_list):
    # num_list.reverse()
    # return num_list
    return num_list[::-1]

print(solution([1, 0, 1, 1, 1, 3, 5]))