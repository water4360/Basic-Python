'''
    input.txt 파일을 읽고 다음 결과 출력
    1. 총 단어 개수 세어보기
    2. 단어의 빈도수를 세고 알파벳 순으로 출력하기
        a 15
        above 1
        blue 1
        ...
    +3. 단어가 몇번째 라인에 나왔는지 출력
        단어a / 15회 / 라인2, 라인3, 5, 11...
'''
from collections import Counter
import re

with open('input.txt', 'r') as file :
    total_words = []
    #라인 분할 & 소문자화 & 특수문자 제거
    for line in file :
        splited_words = line.rstrip('\n').split()
        total_words += [re.sub(r'[^a-zA-Z]', '',word.lower()) for word in splited_words]
        total_words.sort()
    # print(total_words, type(total_words))

    # 총 단어 개수
    # 단어별 빈도수
    cnt_sum = 0
    for word, cnt in Counter(total_words).items() :
        # if word != '' :
        print(f'[{word}] : {cnt}회')
        cnt_sum += cnt

    # print('total_words : ', sorted(total_words))
    print(f'총 단어수 : {cnt_sum}개')