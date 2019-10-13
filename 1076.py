color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
sum1=""

for x in range(3):   
    a = input()
    for y in range(0,10):
        if a in color[y] and x==0:
            sum1 += str(y)
        elif a in color[y]and x==1:
            sum1 += str(y)
            sum1 = int(sum1)
        elif a in color[y] and x==2:
            sum1 *= 10**y
            sum1=str(sum1)
print(sum1)
