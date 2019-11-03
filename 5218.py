test = int(input())
dic={}
i=65
for x in range(1,27):
    dic[chr(i)]=x
    i+=1
for x in range(test):
    a,b=input().split()
    print("Distances:",end=" ")
    for y in range(len(a)):
        if dic[a[y]]>dic[b[y]]:
            print((dic[b[y]]+26)-dic[a[y]],end=" ")
        else:
            print((dic[b[y]])-dic[a[y]],end=" ")
    print()
            
            

    
