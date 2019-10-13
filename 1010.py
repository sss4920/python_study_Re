def fact(n):
    if n==1:
        return 1
    if n==0:
        return 1
    return n*fact(n-1)

def combination(n,m):
    return fact(m)//(fact(m-n)*fact(n))
test = int(input())
for x in range(test):
    m,n=input().split()
    m=int(m)
    n=int(n)
    print(combination(m,n))



    
