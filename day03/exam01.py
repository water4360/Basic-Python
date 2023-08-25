# 230825(금) 문자열
# lower, upper, split, join, strip, just, center, fill, index, find, replace

str = "Hello, World, dear!"
print(str, str.upper(), str.lower())

strList = str.split(sep=',')
print(strList)

str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]') #lstrip : 좌측left 공백 지우기strip
# list화 해서 슬라이싱하기 테스트용ㅎㅎ
# str = list(str)
# str[4:7] = "zzz"
# print(str)

str = '    !   Hello World   dear  my freind     '
print('!중간 여백은 그대로임에 주의!')
print(f'원본str : [{str}]')
print(f'좌측여백지우기 str.lstrip() : [{str.lstrip("! ")}]')
print(f'우측여백 str.rstrip() : [{str.rstrip()}]')
print(f'양측여백 str.strip() : [{str.strip()}]')


str = 'hello'
print(f'str : [{str}]')
print(f'str.center(11) : [{str.center(11)}]')
print(f'str.center(12) : [{str.center(12)}]')
print(f'str.ljust(10) : [{str.ljust(10)}]')
print(f'str.rjust(10) : [{str.rjust(10)}]')
print(f'str.zfill(10) : [{str.zfill(10)}]')

str = 'Hello World!!'
print(f'str.index("o", 6) 6부터 시작해서 o의 idx 반환 : {str.index("o", 6)}')
print(f'str.find("p") p가 없더라도 에러없이 -1반환 : {str.find("p")}')
print(f'str.rfind("o") o의 위치를 우측부터 탐색 : {str.rfind("o")}')
print(f'str.count("l") l의 개수 : {str.count("l")}')
print(f'str.replace("l") l을 => z로 변환 : {str.replace("l", "z")}')



