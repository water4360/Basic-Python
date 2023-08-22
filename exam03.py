'''
제 눈에만 초록색인가여?
'''
# 230822(화)
# 논리값(True, False) 첫글자 대문자에 주의
print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("따옴표 구분할까?", "Hello" == 'Hello')
print("대소문자 다른건?", "Hello" == "hello")
print("1과 1.0의 값비교==는? ", 1 == 1.0)
print("1과 1.0의 타입비교is는?", 1 is 1.0)

# id는 데이터가 저장된 위치값. JS의 해시코드처럼.
print(id('Hello')) #True
print(id('Hello')) #True
print(id('Hello')) #True
# 이 두개는 False
print('id로 1과 1.0을 비교하면 다른 값이 나옴')
print('1 : ', id(1))
print('1.0 : ', id(1.0))


# 오후 수업 13:20
print('0이 아닌 모든 값은 True')
print(bool(int(str(10))))
print(type(bool(int(str(10)))))
print('and 조건의 경우, 참을 만족하는 값을 출력해야 하므로\nabc def가 다 나오지 않고 def만 출력')
msg = "abc" and "def"
print('abc and def : ', msg)
print('or 조건의 경우, abc가 먼저 출력')
msg = "abc" or "def"
print('abc or def : ', msg)
print('\n\n')

#문자열
print('Hello')
print('''Hello''')

print("""Hello
큰 따옴표 3개짜리.
얘는 여러줄 가능.
라인 변경도 가능.
""")

