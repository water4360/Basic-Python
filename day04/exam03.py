# 230828(월)

def solution(sentence) :
    # words = ''
    # wordlist = [w for w in sentence if w not in ['a','e','i','o','u']]
    # for w in wordlist :
    #     if w != ' ' :
    #         words += w
    # return words
    # data2 = [s for s in sentence if s not in 'aeiouAEIOU '] #리스트인 경우 중복 허용
    data2 = {s for s in sentence if s.isalpha() and s not in 'aeiouAEIOU'} #set인 경우 중복 불허
    return data2

print('모음만 빼고 출력 : ', solution("I am a boy, You are a girl!?"))