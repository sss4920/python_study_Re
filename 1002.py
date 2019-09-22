import math
a = int(input())
for x in range(a):
    x1,y1,r1,x2,y2,r2 = map(float, input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d == r2+r1 or d == abs(r2-r1):
        print(1)
    elif d> r1+r2:
        print(0)
    elif d == 0:
        print(0)
    elif d == 0 and r2 == r1:
        print(-1)
    else:
        print(2)
        
