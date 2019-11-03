def prime(n):
    global li1
    flag =True
    if n ==1:
        flag= False
    else:
        for x in range(2,n):
            if n %x ==0:
                flag=False
    if flag:
        li1.append(n)
            
li1=[]
sum1=0
a = int(input())
b = int(input())
for x in range(a,b+1):
    prime(x)
if not li1:
    print(-1)
else:
    mini=min(li1)
    for y in li1:
        sum1+=y
    print(sum1)
    print(mini)
