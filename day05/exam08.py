# 230830(수)
# 외부에서 __붙인 변수는 접근 불가! 비공개화.
# 이런 변수들은 getter, setter 만들어주자.
# setter의 경우 인자에 self외에도 넘어오는 파라미터 받아줘야함을 주의.
# 위장을 위해서는 메소드명 = 변수명 & @property 추가

class Person :
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr

    #만약 사원이 퇴사하는 경우 인원수를 감소시킬 수 있겠지.
    # def __del__(self, count):
        # self.count = count


    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr : {self.__addr}')


    # def getAddr(self):
    #     return self.__addr
    #
    # def setAddr(self, addr):
    #     self.__addr = addr

    #변수 바로 쓰는것처럼 보이게 위장하기.
    @property
    def addr(self):
        return self.__addr

    @addr.setter
    def addr(self, addr):
        self.__addr = addr

p = Person(name='홍길동', age=25, addr='서울')
p.info()

print(p.name)
print(p.age)
# print(p.__addr) #이렇게 사용 불가.
# print(p.getAddr())
print(p.addr)
