# 230830(수)
# static처럼 사용하기

'''
    총 사원수는 0명입니다
    Employee(10, 홍길동, 사원, 3000)
    Employee(20, 고길동, 사원, 3600)
    Employee(30, 장길동, 대리, 4400)
    Manager(100, 부길동, 부장, 7000)
    총 사원수는 4명입니다
'''

class Employee :

    total = 0
    def __init__(self, **kwargs):
        if 'no' in kwargs :
            self.no = kwargs['no']
        if 'name' in kwargs :
            self.name = kwargs['name']
        if 'grade' in kwargs :
            self.grade = kwargs['grade']
        if 'salary' in kwargs :
            self.salary = kwargs['salary']
        Employee.total += 1
        print(f'{self.no}, {self.name}, 직급:{self.grade}, 연봉:{self.salary}')

    def count_total(self):
        print(f'총 사원 수는 {self.total}명 입니다.')

class Manager(Employee) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


print(f'총 사원 수는 {Employee.total}명 입니다.')
e1 = Employee(no=10, name='홍길동', grade='사원', salary='3000')
e2 = Employee(no=20, name='고길동', grade='사원', salary='3300')
e3 = Employee(no=40, name='장길동', grade='대리', salary='4000')
e4 = Manager(no=100, name='부길동', grade='부장', salary='7000')
print(f'총 사원 수는 {Employee.total}명 입니다.')
# Employee.count_total()
