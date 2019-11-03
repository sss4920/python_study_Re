a,b,v = map(int,input().split())
sum1 = 0
day=0

while sum1<v:
    day+=1
    sum1 += a
    if sum1>=v:
        break
    sum1 -= b
print(day)
        
