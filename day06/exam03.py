# 230831(목)
# 예외처리3 - raise 사용자 등록 예외처리

try:
    num = int(input('짝수를 입력하세요 : '))
    if num % 2 :
        raise Exception(f'입력하신 {num}은 짝수가 아니예요')
except Exception as e :
    print(e)
else:
    print(f'입력한 짝수는 {num}')
finally:
    print('어쨌든 프로그램 종료')
    exit(0)
