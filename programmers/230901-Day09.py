# 230901(금) Day09

# 개미 군단
#장군5, 병정3, 일개미1
#5로 나눠서 0이면 5로 나눈 몫
#3으로 나눠서 0이면 3으로 나눈 몫
#아니면 5로 나눈 몫 + 3으로 나눈 몫 + 나머지
# def solution(hp):
#     d5, d3, d1 = 0,0,0
#     while hp != 1 :
#         d5 += hp // 5
#         hp -= d5 * 5
#         d3 += hp // 3
#         hp -= d3 * 3
#         d1 += hp % 3
#         return d5 + d3 + d1
#     return 1
# 모범 답안 - 오직 몫만 생각하는 방식.
# def solution(hp):
#     return hp // 5 + (hp % 5 // 3) + (hp % 5 % 3)
#
# print(solution(999))



#모스부호(1)
# morse = {
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'
# }
# def solution(letter):
#     # return ''.join(i.replace(i, morse.get(i)) for i in letter.split(' '))
#     return ''.join(morse[i] for i in letter.split(' ')) # 모범답안
#
# print(solution(".... . .-.. .-.. ---"))

#가위바위보
#가위2 바위0  보5
#바위0 보 5 가위2
# def solution(rsp):
#     map = {"2":"0", "0":"5", "5":"2"}
#     return ''.join(map[n] for n in rsp)
# # translate와 maketrans를 활용한 참고답안
# def solution(rsp):
#     return rsp.translate(str.maketrans('025', '502'))
# print(solution("205"))



#접미사 배열
# def solution(my_string):
#     data = [my_string[w:] for w in range(len(my_string))]
#     return sorted(data)
#
# print(solution("banana"))


#접미사인지 확인하기
# def solution(my_string, is_suffix):
#     return 1 if my_string.endswith(is_suffix) else 0
# #사고적으로 흥미로운 답안
# def solution(m, s):
#     if m[-len(s):]==s: return 1
#     return 0
#
# print(solution("banana", "ana"))


#부분 문자열 이어 붙여 문자열 만들기
# def solution(my_strings, parts):
#     return ''.join(my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(len(parts)))
# 참고 답안 - 문자열 += 쓰고 싶으면
# def solution(my_strings, parts):
#     answer = ""
#     for i in range(len(parts)):
#         answer += (my_strings[i][parts[i][0]:parts[i][1] + 1])
#     return answer
#
# print(solution(["progressive", "hamburger", "hammer", "ahocorasick"],
#                [[0, 4], [1, 2], [3, 5], [7, 7]]))


#배열 만들기 5
# def solution(intStrs, k, s, l):
#     answer = []
#     for n in intStrs :
#         if int(n[s:s+l]) > k :
#             answer.append(int(n[s:s+l]))
#     return answer
# print(solution(["0123456789","9876543210","9999999999999"], 50000,5,5))


#구슬을 나누는 경우의 수
# n개 중 m개를 뽑는 경우 (5개, 3개)
# 5-3
# import math
#
# def solution(balls, share):
#     return math.comb(balls, share)
#
# print(solution(3,2))
# print(solution(5,3))
