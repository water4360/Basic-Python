# 230828(월)
'''
    def 함수([인자, 인자...]) :
        문장
        return
'''
def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def div(a, b) :
    return a // b

print(f'덧셈 : {add(12, 7)}')
print(f'뺄셈 : {sub(12, 7)}')
print(f'곱셈 : {mul(12, 7)}')
print(f'눗셈 : {div(12, 7)}')

def calculate(a, b) :
    return add(a, b), sub(a, b), mul(a, b), div(a, b)

print(type(calculate(12, 7)), calculate(12, 7))

# list = calculate(12, 7) # 이렇게 받을 수도 있지만.
a, b, c, d = calculate(12, 7) # 언팩킹unpacking으로 이렇게도 가능하다!!