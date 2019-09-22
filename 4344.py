test = int(input())
for x in range(test):
    sum1 = 0 # 평균 구하려고 쓰는 합
    person = 0
    pyoung = 0
    number = 0
    b = input().split()
    b = list(map(int,b))
    for y in range(1,b[0]+1):
        sum1 += b[y]
        pyoung = sum1/b[0]
    for z in range(1,b[0]+1):
        if b[z] > pyoung:
            number += 1
            person =number/b[0]
    print('%.3f%%'%round(person*100,3))
    
    
    
