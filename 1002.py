import math
a = int(input())
for x in range(a):
    x1,y1,r1,x2,y2,r2 = map(float, input().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d == 0: # 중심이 같을때
        if r1 != r2:# 중심이 같은 원안에 원이라 안만남
            print(0)
        if r1 == r2:# 동심원
            print(-1)
    else:# 중심이 다를때
        if r2+r1 > d:# 만약 반지름 두개 합한 값이 두 중심사이의 거리보다 길면
            if abs(r2-r1)<d: # 반지름 차가 두 중심사이의 거리보다 짧을때
                print(2)
            elif abs(r2-r1)==d:# 내접할 때
                print(1)
            else:# 그냥 한 원이 다른 원 안에서 만나지도 않고 두둥실 떠다닐때
                print(0)
        elif r2+r1 <d: # 두원이 그냥 겁나 떨어져있을때
            print(0)
        elif r2+r1 == d:# 두원이 외접할때
            print(1)
        
        
   
        
