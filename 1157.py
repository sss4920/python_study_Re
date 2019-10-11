a = input()
maxi = 0
mini = 0
for i in range(65,130):
    if i >=97:
        i=i-32
        i = chr(i)
        if a.count(i) >= maxi:
            maxi = a.count(i)
            mini = i
        i = int(i)    
        i=i+32
    else:
        i = chr(i)
        if a.count(i) >= maxi:
            maxi = a.count(i)
            mini = i
print(mini)
