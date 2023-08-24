import random

num = random.randint(250, 300)
print(f'추출된 난수 : {num}')

print('<게임 369, 369!!>')
for i in range(1, num+1) :

    n1 = i % 10 #1의 자리
    n10 = i // 10 #10의 자리
    print(f'{i:<3}', end=' ') #<3은 3칸 좌측정렬, >3은 우측정렬
    if not n1 :
        print('뽀' * n10, '숑', end='', sep='')
    if n1 in [3, 6, 9] :
        print('짝', end='')
    if n10 in [3, 6, 9] :
        print('짝', end='')
    print()

data = [2, 5, 9]
print(data)

data = list()
print(data)