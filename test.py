# 1111번
# dict에 있는 단어로 분리할것
# 분리 기준이 되는 sep단어의 첫 글자와, 앞 단어의 마지막 글자가 일치할 것
# 가능한 많은 단어로 분리된 경우의 단어수.

# 첫번째 시도, 구분자별로 찾기
# def solution(s, word_dict):
#     answer = 0
#     split_arr = []
#     #구분자를 돌면서
#     for w in word_dict:
#         print('찾을 단어w:', w)
#         #w가 s에 있으면 배열에 추가하고, 문자에선 없애고.
#         if w in s:
#             print(f'{w}가 존재함')
#             #
#             split_arr.append(w)
#             s = s.replace(w, ''.join(w[-1]))
#             #하지만 앞의 w가 나머지 s를 분리하지 못하는 경우
#
#             print(s)
#         # print(split_arr)
#     return answer



#두번째 시도,
# def solution(s, word_dict):
#     answer = 0
#     words_arr = []
#     for w in word_dict:
#
#     return answer


# print('result :', solution("centerminus", ["cent", "center", "term", "terminus", "rm", "min", "minus", "us"]))





# 22222번
# 원소를 꼭 다 구할 필요 있나? 경우의 수만 나오면 될것.
# 각각 다른 국가집합. 집합의 원소.
# 존재하는 국적이면 확장, 신규 국가라면 추가.
def solution(n, nationality):
    answer = []
    for sub_arr in nationality:
        duplicated = False

        for group in answer:
            if any(student in ):
                group.extend(sub_arr)
                print(group)
                duplicated = True
                break
        if not duplicated:
            answer.append(sub_arr)
    return answer


print('정답', solution(5, [[1,2],[1,3],[3,4]]))
