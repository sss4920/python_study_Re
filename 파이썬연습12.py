test = int(input())
for x in range(test):
    a,b = input().split(" ")
    a=int(a)
    b=int(b)
    sum = a+b
    print("Case #%d:"%(x+1),"%d +"%a,"%d ="%b,sum)
