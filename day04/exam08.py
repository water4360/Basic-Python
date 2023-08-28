# 230828(월)

data = [10,20,30,40]
print(data) #[10, 20, 30, 40]
print(*data) # 10 20 30 40


def getTotal(a, b, c, d) :
    return a+b+c+d

def getSum(*nums) :
    s = 0
    for n in nums :
        s += n
    # print(nums, type(nums))
    return s

print(f'total1 : {getTotal(1, 2, 3, 4)}')
print(f'total2 : {getTotal(*[1,2,3,4])}')
print(f'total3 : {getTotal(*data)}')

print(f'sum1 : {getSum(10,20,30,40)}')
print(f'sum2 : {getSum(10,20,30,40,50,60)}')
print(f'sum3: {getSum(10,20)}')
