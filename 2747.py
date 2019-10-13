import sys
sys.setrecursionlimit(10000)

a = int(input())
b =[0,1]
i=2
while(i<=45):
    b.append(b[i-1]+b[i-2])
    i+=1        
print(b[a])
        
