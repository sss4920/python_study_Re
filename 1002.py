import math
a = int(input())
for x in range(a):
    x1,y1,r1,x2,y2,r2 = map(float, input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d<r2+r1 and r2-r1< d:
        print(2)
    elif abs(r2-r1) == d or r2+r1 == d:
        print(1)
    elif (d > r1+r2) or (d>abs(r2-r1)):
        print(0)
    elif (r1 == r2) & (d == 0):
        print(-1)
    elif d<r2-r1:
        print(0)
    else:
        print(2)
        
   
        
