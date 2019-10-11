string = input()
di = {}
number = 97


for z in range(0,26):
        di[chr(number)] = -1
        print(chr(number))
        number +=1
number = 97
for x in range(0,26):# 방리스트 만들기
        for y in range(len(string)):#문자열 인덱스 돌리기
                if string[y] == di[chr(number)]:
                        di[chr(number)] = x
                else:
                        di[chr(number)] = -1
        number +=1
        if number == 123:
                break
        
print(di)
