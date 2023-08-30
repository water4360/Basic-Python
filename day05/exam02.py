def print_book(title, writer, price) :
    print(f'제목 : {title}')
    print(f'작가 : {writer}')
    print(f'가격 : {price}')
    pass


print_book('홍길동전', '허균', 15000)
print_book(title = '홍길동전', writer = '허균', price = 15000)
print_book(price=23000, writer='허균', title='[양장본]홍길동전')

book = {'title':'우리가 빛의 속도로 갈 수 없다면', 'writer':'김초엽', 'price':19000}

print('<별2개>')
print_book(**book)
print('<별1개> : 딕셔너리일때 key값을 가져오게 된다.')
print_book(*book)