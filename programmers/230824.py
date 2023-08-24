# 230824
# 문자열 분리해서 하나씩 출력하기
# str = 'abcde'
# for i in iter(str) :
#     print(i)


# 홀짝 구분하기
# a = 10
# print(f'{a} is odd') if a % 2 else print(f'{a} is even')


# 분수의 합을 기약 분수로 나타내기
# import math
#
# #분자1 & 분모1
# num1 = 1
# denom1 = 2
#
# #분자2 & 분모2
# num2 = 3
# denom2 = 4
#
# mom = (denom1 * denom2)
# son = (num1 * denom2) + (num2 * denom1)
#
# #분모 최대공약수
# denom_gcd = math.gcd(mom, son)
# answer = [son // denom_gcd, mom // denom_gcd]
# # print(son // denom_gcd)
# # print(mom // denom_gcd)
# # print(denom_gcd)
# print(answer)







#배열 두배 만들기
# numbers = [1, 2, 100, -99, 5]
#
# answer = []
# for i in numbers :
#     answer.append(i * 2)
# print(answer)


#문자열 겹쳐쓰기
# my_string = "aaaaaa"
# overwrite_string = "bbb"
# s = 3
# 문자열의 시작점s에서부터 overwrite의 길이만큼의 문자를 찾아서
# 교체.
# part = my_string[s:s+len(overwrite_string)]
# print(part)
# answer = my_string[:s]+overwrite_string+my_string[s+len(overwrite_string):]
# print(answer)