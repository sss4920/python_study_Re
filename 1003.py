import sys

def fibonacci(n):
    global zero,one
    if n== 0:
        zero +=1
        return 0
    elif n==1:
        one +=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
test = int(input())
for x in range(test):
    zero,one=0,0
    a = int(sys.stdin.readline())
    fibonacci(a)
    print("%d %d"%(zero,one))
