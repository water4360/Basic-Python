#230828(월)

print('< 읽어온 데이터 출력 >')
# 방법1
# with open('test02.txt', 'r') as file :
#     while True :
#         line = file.readline().rstrip('\n')
#         if line == '' :
#             break
#         print(f'[{line}]')

# 방법2
with (open('test02.txt', 'r') as file) :

    for line in file :
        print(line.rstrip('\n'))

    # line = file.readline().rstrip('\n')
    # while line != '' :
    #     line = file.readline().rstrip('\n')
    #     print(line)
