# 230830(수)

class Car:
    addr = '서울'

    #아무거나 못넣도록 이렇게 제한할 수도 있음.
    __slots__ = ['name', 'price', 'company']
    def __init__(self, **kargs):
        if 'name' in kargs :
            self.name = kargs['name']
        if 'price' in kargs :
            self.price = kargs.get('price')
        if 'company' in kargs :
            self.company = kargs.get('company')
            Car.addr = '제주'

    def info(self):
        print(f'[{self.name}]의 가격은 {self.price}만원')


c = Car(name='그랜저', price=4000, company='현대')
c2 = Car(name='모닝', price=2000)
c.info()
c2.info()
# company가 있는 c만 바뀌어야겠지만
# static처럼 Car로 써서 c2도 바뀌는 것.
print(c.addr)
print(c2.addr)