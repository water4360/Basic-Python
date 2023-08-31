# 230831(목)
# 예외처리2 - else, finally
import random

try:
    num = random.randint(0, 2)
    result = 10//num
except Exception as e: #예외가 발생하면
    print('예외발생 : ', e)
else: #예외가 발생하지 않으면
    print(f'10//{num} = {result}')
    pass
finally:
    print('프로그램 종료')
    pass