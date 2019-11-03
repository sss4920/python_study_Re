a= int(input())
count=0
for x in range(a):
    sen = input()
    li1=[]
    flag=True
    for y in range(len(sen)):
        if sen[y] in li1:
            if sen[y-1] == sen[y]:
                continue
            else:
                flag=False
                break
        else:
            li1.append(sen[y])
    if flag:
        count+=1
print(count)
    
            
        
        
