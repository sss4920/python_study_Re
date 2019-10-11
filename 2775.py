a = []
number = 1
for i in range(14):#이게 층
    k= []#이게 호실이었네
    for j in range(14):#이게 호실에 채워
        if i==0:
            k.append(number)
            number+=1
        else:
            sum1 = 0
            if j ==0:
                a[i][j]=1
            else:    
                for z in range(0,j):
                    sum1 += a[i-1][z]
                    k.append(sum1)
    a.append(k)
print(a)

