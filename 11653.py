a = int(input())
b = []
k = 2
while True:
    if a ==1:
        b.sort()
        for x in b:
            print(x)
        break
    if a % k ==0:
        b.append(k)
        a =a //k
    else:
        k +=1
        
    
