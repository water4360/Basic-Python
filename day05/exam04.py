# 230830(수)
# class에 대하여.


class Dog :
    pass

dog = Dog()
print('dog의 클래스는?:', type(dog))





# 클래스 내에 내장함수가 필요하겠죠.
# 첫번째 인자는 self(호출한 객체)를 무조건 가지고 있음.
# 누가 불렀는지 알아야 하기 때문.
# java에서의 this와 같은 개념.
class Car :
    def __init__(self):
        print('Car 객체 생성완료!')

    def drive(self) :
        # print(self)
        print('부웅~ 운전해요')

c = Car()
# print(c)
c.drive()

#type(10)=='int, type('111)=='str' 이렇게 타입확인하는 것? 불가
# 그래서 나온 것이 isinstanceof
# 예시 : isinstance(10, int), isinstance('111', str)
# 아웃풋은 boolean

print(f'type(Car) 여부 : {isinstance(c, Car)}')
print(f'type(Car) 여부 : {isinstance(10, Car)}')
print(f'type(Car) 여부 : {isinstance([10,20,30], Car)}')

