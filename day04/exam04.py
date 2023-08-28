# 230828(월)
'''
    byteStream, 같은 것처럼
    open(파일명, 모드값) # "r", "w" 둘 중 하나
    read()/write()
    close()

    with open() as 파일객체 :
         data = read()/write()
'''
# file = open('test.txt', "w")
# file.write('hello')
# file.close() # open을 했으면 꼭 닫아줘야...

# file = open('test.txt', 'r')
# data = file.read()
# file.close()

#자동으로 닫아주는
with open('test.txt', 'r') as file :
    data = file.read()

print(f'읽어온 데이터 : {data}')