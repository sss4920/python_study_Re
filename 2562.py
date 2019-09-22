b = [1,2,3,4,5,6,7,8,9]
maxi = 0
number = 0
for x in range(0,9):
    b[x] = int(input())
    if b[x] > maxi:
        maxi = b[x]
        number = x
print(maxi)
print(number+1)
    
