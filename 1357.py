def Rev(X):
    temp=X[-1::-1]
    return int(temp)
a,b = input().split()

print(Rev(str(Rev(a)+Rev(b))))
