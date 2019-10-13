M=int(input())
N=int(input())
big=[]
i=1
sum1=0
x=0
while True:
    if i**2>=M and i**2<=N:
        big.append(i**2)
        sum1+=big[x]
        x+=1
        i+=1
    elif i**2<M:
        i+=1
        continue
    else:
        break
if sum1==0:
    print(-1)
else:
    print(sum1)
    print(big[0])

    
