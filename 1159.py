num = int(input())
name=[]
last=[]
result=[]
i=65
k=""
for x in range(num):
    name.append(input())
for x in name:
    last.append(x[0])
for x in range(32):
    temp=last.count(chr(i+32))
    if temp>=5:
        result.append(chr(i+32))
    i+=1
if len(result)==0:
    print("PREDAJA")
else:
    for y in range(len(result)):
        k+=result[y]
    print(k)
