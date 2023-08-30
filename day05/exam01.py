# 230830(수)
# 언패킹unpacking

# print메서드에는 기본적으로 *values라고 되어있음.
# print(10, 20, 30, 40, 'aaa', end='', sep='')

# 인자가 없으면 end='\n', sep=' '가 default
# 인자를 정의할 때는 가변인자(*values) 뒤에.
def myPrint(*values, end='>') :
    for value in values :
        print(value, end=end) # end를 추가해줘야.

myPrint(10, end='\n')
myPrint(10, 'A')
myPrint('튜플형태:', (10,20,30,40), '딕셔너리형태:', [100,200,300,400])
print()

def calc(way, *values) :
    result = 0
    if way == 'add' :
        for n in values :
            result += n
    if way == 'mul' :
        result = 1
        for n in values :
            result *= n
    if way == 'div' :
        for n in values :
            result = n

    return result


def calc(command, *args) :
    # print('command : ', command)
    # print('args : ', args)
    s = 0 if command == 'add' else 1
    for value in args :
        if command == 'add' :
            s += value
        elif command == 'mul' :
            s *= value

    return s




print(calc('add', 12, 7))
print(calc('add', 12, 6, 9))
print(calc('mul', 12, 7))
# print(calc('add', 12, [6, 9, 10], 30)) # 고민해볼 것!!!
print(calc('mul', 1, 2, 3, 4, 5))
# print(calc('div', 10, 5))