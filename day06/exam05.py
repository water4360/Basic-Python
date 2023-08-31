# 230831(목)
# 상속을 통한 사용자정의 예외 클래스 만들기
class NotEvenException(Exception) :
    def __init__(self, msg):
        # 만들어져있는 msg 쓰기
        super().__init__(msg)


def get_number():
    try:
        num = int(input('짝수를 입력하세요 : '))
        if num % 2:
            raise NotEvenException(f'입력하신 {num}은 짝수가 아니예요')
    except:
        print('get_number() 예외 발생!')
        raise # 이미 처리중인 예외를 떠넘기고 싶을때.
    return num

try:
    num = get_number()
    print(num)
except NotEvenException as e :
    print(e)