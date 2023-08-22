# 0~9까지의 데이터 집합
data = list(range(1, 10))
print(data)

# slice : 0번지부터 5번지 직전까지의 데이터 출력
print(data[0:5])

# 원본은 두고, 잘라낸 데이터값을
data2 = data[0:5]
print('원본 : ', data)
print('복사본 : ', data2)
print(data[5:8])
print(data[:3])
# 길이를 구하는 함수 len()
print(data[3:])  # print(data[3:len(data)])와 동일.

print(data[:])
print('슬라이스 된 데이터 : ', data)
# 그대로 적용하면 shallow copy
data2 = data
print('shallow copy : ', data2)
# 슬라이스를 하면 deep copy
data2 = data[:]
print('deep copy : ', data2)
data2[0] = 100
print(data)
print(data2)

# -1의 경우, print(data[5:len(data)-1])과 동일함. 축약된 것.
print(data[5:len(data)])  # 결과 : [6,7,8,9]
print(data[5:-1])  # 결과 : [6,7,8]

# 리스트명[시작=0:종료=len(리스트):간격=1]
# 콜론 다중사용도 가능. 2에서 8번지까지 2씩 증가.
print(data[2:8:2])  # 결과 : [3,5,7]
print(data[2::2])  # 결과 : [3,5,7,9]
print(data[8:2:-2]) # 결과 : [9, 7, 5]
print(data[::-1]) # 결과 : [9, 8, 7, 6, 5, 4, 3, 2, 1]

print('data : ', data)
# 범위 밖의 데이터 접근하려하면 에러남.
# 당연히. 우리는 1~9까지만 만들었으므로.
# data[15] = 100
# print('data : ', data)

## 웬만한 경우에도 에러발생하지 않고 유연하게 적용되는....
# data[2:5] = [100, 200, 300]
# data[2:5] = [100] # [1, 2, 100, 6, 7, 8, 9]
# data[2:5] = [100, 200, 300, 400, 500] # [1, 2, 100, 200, 300, 400, 500, 6, 7, 8, 9]
data[2:6:2] = [10, 20] # [1, 2, 10, 4, 20, 6, 7, 8, 9]
print('유연한 적용 : ', data)


del data[2:3] # [1, 2, 4, 20, 6, 7, 8, 9]
# del data[2:5] #[1, 2, 6, 7, 8, 9]
print('슬라이스를 활용한 삭제 : ', data)