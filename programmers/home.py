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
def solution(num_list, n):
    answer = [[]]
    for n in range(len(num_list)//n) :
        answer.append(num_list[:n*2])

    return answer
print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))