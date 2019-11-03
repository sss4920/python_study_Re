a,b=input().split()
num1=[]
num2=[]
for x in range(len(a)):
    num1.append(a[x])
    num2.append(b[x])
temp1=num1[0]
temp2=num2[0]
num1[0]=num1[2]
num2[0]=num2[2]
num1[2]=temp1
num2[2]=temp2
s1=num1[0]+num1[1]+num1[2]
s2=num2[0]+num2[1]+num2[2]
result=max(int(s1),int(s2))
print(result)
    
    
    
    
