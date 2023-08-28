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

with open('input.txt', 'r') as file :
    cnt_words = 0
    total_words = []

    for line in file :
        words = line.rstrip('\n').split()
        cnt_words += len(words)
        print(words)
        total_words += [word.lower() for word in words if word.isalpha()]

    cnt_sum = 0
    for word, cnt in Counter(total_words).items() :
        print(f'{word} : {cnt}개')
        cnt_sum += cnt

    print('total_words : ', sorted(total_words))
    print('cnt_sum : ', cnt_sum)

    print('개수 : ', cnt_words)
