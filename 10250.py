test = int(input())
for x in range(test):
    floor,room,person=map(int,input().split())
    first =[]
    i=1
    for a in range(i,room+1):
        for b in range(1,floor+1):
            first.append(b*100+a)
    print(first[person-1])
            
            
        
    
