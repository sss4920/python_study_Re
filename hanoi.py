a = int(input())
if a > 20:
    print(2**a - 1)
else:
    print(2**a - 1)
    for x in range(1,2**a):
        if x % 2 == 0:
            print(1,3,end = " ")
            print()
        
