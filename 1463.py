"""
아직 미해결
"""
x = int(input())
number = 0
for y in range(x):
    if x == 1:
        break
    elif x  % 5 ==0:
        x = x //5
        number += 2
    elif x % 3 ==0:
        x = x//3
        number += 1
    elif x %2 == 0:
        x =x//2
        number += 1
    else:
        x = x-1
        number +=1
print(number)
    
