# 230830(수)
# 상속


class Parent :
    def __init__(self):
        self.name = '부모'
        print('Parent() 호출...')
    def info(self):
        print('Parent info() 호출...')

class Child(Parent) :
    def __init__(self):
        super().__init__() # 파이썬에서는 따로 super를 호출해줘야 함.
        print('Child() 호출...')
    pass

    def info(self): #오버라이딩?
        super().info()
        print('Child info() 호출...')

# p = Parent()
p = Child()
p.info()
print(p.name)


