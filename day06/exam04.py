# 230831(목)
# 예외처리4
# 함수 내에 raise를 넣어도
# 호출한 부분까지 예외처리가 넘어감.
# 그러므로 try, except로 감싸줌.
#
def get_number() :
    try :
        num = int(input('짝수를 입력하세요 : '))
        if num % 2:
            raise Exception(f'입력하신 {num}은 짝수가 아니예요')
    except:
        print('get_number() 예외 발생!')
        raise # 이미 처리중인 예외를 떠넘기고 싶을때.
    return num

try:
    num = get_number()
    print(num)
except Exception as e :
    print(e)