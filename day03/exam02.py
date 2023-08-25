#0825(금) 딕셔너리

#
data = {'hong' : 1111,
        'kang' : 2222,
        'han' : 3333,
        'park' : 4444,
        'kang' : 5555,
        100 : '123'} #key에 꼭 문자만 들어가야하는 것은 아님.
print('data : ', data, type(data))

stuInfo = {'name' : 'hong',
           'age' : 28,
           'scores' : [100, 90, 70]}
print('stuinfo : ', stuInfo)

#딕셔너리를 만드는 두가지 방법
data = {}
data = dict()
data = dict(name='hong', age=28, addr='seoul')
print('data: ', data, type(data))

#이렇게 튜플로 만드는 경우에는 정수(100)가 key가 될 수 있음.
data = dict([('name', 'hong'), ('age', 28), ('addr', 'seoul'), (100, 'max')])
print('dict에 튜플을 넣은 data: ', data)

data = dict(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))
print('dict에 zip을 넣은 data: ', data)