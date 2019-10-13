def is_prime(a):
    i=2
    if a==1:
        return False
    while i<a:
        if a % i==0:
            return False
        else:
            i+=1
            continue
    return True
a= int(input())
print(is_prime(a))
        
            

