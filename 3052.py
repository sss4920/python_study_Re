a = []
number = 0
for x in range(10):
    b =int(input())
    b = b % 42 
    a.append(b)
a = set(a)
for x in a:
    number +=1
print(number)

