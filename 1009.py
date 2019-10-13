def division(a,b):
    sum1=1
    while b!=0:
        if b >30:
            if ((a**30)%10)==0:
                sum1*=10
                b-=30
            else:    
                sum1*=(a**30)%10
                b-=30
        else:
            if ((a**30)%10)==0:
                sum1*=10
                b-=30
            else:
                sum1*=(a**b)%10
                return sum1

test = int(input())        
for x in range(test):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(division(a,b))
            
        
