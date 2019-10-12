import sys
sys.setrecursionlimit(10000)

def onenumber(a):
    global count
    b =[]
    if len(a)>=3:
        for x in range(len(a)):
            b.append(int(a[x]))
        temp=0
        for y in range(len(a)-1):
            if y==0:
                rtemp=b[y+1]-b[y]
            else:
                if b[y+1]-b[y] != rtemp: # 한수가 아니다
                    return False
                else:
                    continue
        return True

a = int(input())
count = 99
if a <=99:
    print(a)
else:    
    for x in range(100,a+1):
        x=str(x)
        temp = onenumber(x)
        if temp:
            count+=1
    print(count)
        
        
        
                    
