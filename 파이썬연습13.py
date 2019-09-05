N = input()
N = int(N)
kg3 = 0
kg5 = 0
while (N >= 5):
    N = N - 5
    kg5 = kg5 +1
while (N >= 3):
    N = N - 3
    kg3 = kg3 + 1

if(N != 0):
    print(-1)
elif(N == 0):
    print(kg5 + kg3)
