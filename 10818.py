a = int(input())
b = []
b = input().split(" ")
maxi = int(b[0])
mini = int(b[0])
b = list(map(int,b))
for x in range(0,a):
    if b[x] >= maxi:
        maxi = b[x]
    if b[x] <= mini:
        mini = b[x]
print(mini,maxi,end = " ")

    
    

