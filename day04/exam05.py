# 230828(월)

# quit이 나올때까지 문자열을 입력받아 test02.txt에 저장 후
# test02.txt에 저장된 모든 문자열을 읽어서 출력하기.



# with open('test02.txt', 'w') as file :
#     print('문자열 입력하세요. q 입력시 종료 >> ')
#     while True :
#         msg = input()
#         if msg == 'q' :
#             break
#         else :
#             # file.write('{0}\n'.format(msg))
#             file.write(f'{msg}\n') # print에서만 포맷팅 f''쓰는게 아니라는 점~
# print('test02.txt 저장 완료...')

print('< 읽어온 데이터 출력 >')
# with open('test02.txt', 'r') as file :
#     # for i in range(3) : # 3줄인거 알고 불러오는건 말도 안되는~
#         # msg = file.read()
#         # print(msg)
#     # lines = file.readlines() # 리스트list를 불러오고
#     lines = file.readline() # 첫줄 문자열str만 불러오고
#     for line in lines :
#       print(line.rstrip('\n'))




