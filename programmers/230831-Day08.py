#230831(목)



# 입문부터
# 배열자르기
# def solution(numbers, num1, num2):
#     return numbers[num1:num2+1]
#
# print(solution([1, 2, 3, 4, 5],1,3))


# 외계행성의 나이
# def solution(age):
#     answer = ''
#     words = 'abcdefghij'
#     for i in str(age) :
#         answer += words[int(i)]
#         # print(answer)
#     return answer
# print(solution(10))


# 진료 순서 정하기
# 작은 순서대로 값을 넣고. emergency의 숫자의 인덱스를 구해보자.
# def solution(emergency):
#     answer = []
#     #큰것부터 순차적으로. 76,24,3
#     sort_e = sorted(emergency, reverse=True)
#     for n in emergency :
#         answer.append(sort_e.index(n)+1)
#     return answer
# 리팩토링 key랑 value를 함께 제공하는 enumerate 활용
# def solution(emergency):
#     answer = []
#     sort_e = sorted(emergency, reverse=True)
#
#     #value:key 구조. 단, 인덱스는 1부터 시작하도록.
#     map = {v:i+1 for i, v in enumerate(sort_e)}
#
#     #emergeny의 값들이 map의 몇번째인지.
#     for n in emergency :
#         answer.append(map[n])
#     return answer

# print(solution([3, 76, 24]))
# print(solution([30, 10, 23, 6, 100]))


# 순서쌍의 개수 ***
# from collections import Counter
# def solution(n):
#     answer = 0
#     data2 = []
#     #공약수들
#     data = [i for i in range(1, n+1) if n % i == 0]
#     # for i in range(len(data)) :
#     #     data2 += [(data[i], data[-i])]
#     # print(data2)
#     return len(data)
# 진짜 순서쌍을 구해야 한다면.
# def solution(n):
#     answer = 0
#     #공약수들
#     data = [i for i in range(1, n+1) if n % i == 0]
#     data2 = []
#     for i in data :
#         data2.append((i, n//i))
#     print(data2)
#     return len(data2)
#
# print(solution(100))





# 간단한 논리 연산
# def solution(x1, x2, x3, x4):
#     return (x1 or x2) and (x3 or x4)
# print(solution(False, True, True, True))
# print(solution(False, True, True, True))


# 주사위 게임 3 ********
# 교집합??
# 배열의 숫자를 센다. 개수를 키로 잡고 눈금을 값으로??
from collections import Counterdef solution(a, b, c, d):
    data = sorted([a,b,c,d])
    ul = list(set(data))
    print('정렬data : ', data)
    print('유니크data : ', ul)

    #모두 같다면 1111 * p
    if len(ul) == 1 :
        return 1111 * a

    #전부 다르면 제일 작은 숫자.
    if len(data)==len(ul) :
        return min(data)

    # for n, c in Counter(data).items() :
    #     print(f'n = {n}, c = {c}')

    if len(ul) == 2 :
            #2개씩 같다면 (p+q) * |p-q|
            if data[1] != data[2] :
                # print('여기')
                return (ul[0]+ul[1])*abs(ul[0]-ul[1])
            else :
                #p3개 같고 q1개 다르면 (10 * p + q)제곱
                if data.count(ul[0]) == 3 :
                    return (10 * data[0] + data[3])**2
                else :
                    return (10 * data[3] + data[0])**2

    #p2개 같고 q, r 다르면 q * r
    if len(ul) == 3 :
        for n in data :
            if data.count(n) == 2 :
                ul.remove(n)
                return ul[0] * ul[1]

print('정답 : ', solution(4,4,4,1))
print('정답 : ', solution(1,1,1,4))
print('정답 : ', solution(6,3,3,6))
print('정답 : ', solution(2,5,2,6))



# 글자 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181915
# def solution(my_string, index_list):
#     answer = ''
#     for i in index_list :
#         answer += my_string[i]
#     return answer
# join 활용예시
# def solution(my_string, index_list):
#     return ''.join(my_string[i] for i in index_list)
#
# print(solution("zpiaz",[1, 2, 0, 0, 3]))



# 9로 나눈 나머지
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
# def solution(number):
#     nums = [int(c) for c in number]
#     return sum(nums)%9
# 꼭 리스트를 안만들어도.
# def solution(number):
#     num = 0
#     for c in number :
#         num += int(c)
#     return num%9
#
# print(solution("123"))


# 문자열 여러 번 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181913
# def solution(my_string, queries):
#     # 문자열 분할
#     data = [w for w in my_string]
#     print('분할 원본 :', data)
#     # print(data[::-1])
#
#     # s,e는 범위 제공.
#     # 쿼리 돌면서 순서를 바꿨으면
#     for s, e in queries :
#         # print(s, e)
#         data[s:e+1] = reversed(data[s:e+1])
#         # data[s:e+1] = data[s:e+1][::-1] # 모범답안 참고
#         # print(data) #이렇게 범위를 바꾸고.
#     return ''.join(data)
#
# print(solution('rermgorpsam', [[2, 3], [0, 7], [5, 9], [6, 10]]))