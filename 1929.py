a,b =map(int,input().split())
for x in range(a,b+1):
    flag = True
    if x ==1:
        flag = False
    else:
        for y in range(2,x):
            if x % y ==0:
                flag=False
    if flag:
        print(x)

