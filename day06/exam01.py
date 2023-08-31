# 230831(목)
# 예외처리 try~except

import random
try: #예외가 발생할 문장
    num = random.randint(0,3)
    print('추출된 난수 : ', num)
    print(10//num)
    data = [10,20]
    print(data[2])
except ZeroDivisionError as e:
    #발생시 처리
    print('ZeroDivisionError : 0으로 나눌 수 없어요', e)
except IndexError as e:
    print('IndexError : 인덱스 범위를 초과했어요', e)
except Exception as e :
    print('Exception', e)