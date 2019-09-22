li1 = list(map(int,input().split()))
li2 = li1[:]
li3 = li1[:]
for x in range(0,8):
    li2.sort()
    li3.sort(reverse=True)
    if li1 == li2:
        print("ascending")
        break
    elif li1 ==li3:
        print("descending")
        break
    else:
        print("mixed")
        break
    
        
