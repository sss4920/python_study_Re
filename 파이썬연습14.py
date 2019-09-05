test, small =input().split(" ")
test = int(test)
small = int(small)
list2 = []
for x in range(test):
    list = []
    a = input().split(" ")
    a = int(a)
    if a < small:
        list2.append(a)
print(list2, end=" ")
