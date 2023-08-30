# 230830(수)

# key는 없이 value만 있는 경우
# def print_book_args(*args) :
#     print(args)
#     pass
# print_book_args('파과', 15000)
# print_book_args('파과', '구병모', 15000)



# def print_book_info(title, writer, price) :
def print_book_info(**args) : # kargs라고 되어있는 경우는 다 딕셔너리 형태. key의 k.
    for key, value in args.items() :
        print(f'{key} : {value}')
    print('='*20)


print_book_info(title ='파과', writer='구병모', price=18000)
print_book_info(writer='구병모', title ='파과')
print_book_info(title ='파과')
print_book_info(title ='파과', price=18000)

book = {'title':'우리가 빛의 속도로 갈 수 없다면', 'writer':'김초엽', 'price':19000}
print(*book.items())
# print_book_info(**book)