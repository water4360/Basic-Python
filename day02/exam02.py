#230823
#    sort    : 정렬 (임시정렬 sorted(data), 원본적용 data.sort() 구분할 것)
'''
    무작위 데이터의 최소값과 최대값을 구한다고 한다면.
'''
data = [10, 40, 20, 70, 50, 60, 30, 50]

sortedData = sorted(data)
maxi = sortedData[-1]
mini = sortedData[0]

print(f'최대값 : {maxi}, 최소값 : {mini}')
print(f'내장max : {max(data)}, 내장min : {min(data)}')
print(f'내장sum : {sum(data)}')