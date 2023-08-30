# 230830(수)
# 클래스와 변수와 self와 함수

class TV :
    def __init__(self):
        # print('TV 클래스 초기화 진행')
        self.power = False
        self.channel = 10
        print('self : ', self)

    def info(self):
        print(f'채널정보 : {self.channel}')
        if 'volume' in self.__dict__ :
            print(f'음량 : {self.volume}')

# stv = TV()
# ltv = TV()
# print('stv :', stv)
# print('ltv :', ltv)


# 원래라면 함수내의 변수를 갖다 쓸 수 없겠지만
# __init__에서 self 키워드를 붙여주면 멤버변수처럼 쓸 수 있음!
# self.power가 아니라 그냥 power로 바꿔보면 이해가능.
tv = TV()
print(tv.power)
print('<volume추가 전 info>')
tv.info()
tv.volume = 20
print(tv.volume)
print('<volume추가 후 info>')
tv.info()


class Car :
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print(f'모델명 {self.name}의 가격 : {self.price}만원')

c = Car('그랜저', 4000)
c2 = Car('모닝', 2000)

c.info()
c2.info()






