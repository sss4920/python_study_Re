a=0
b=0
while (True):
    try:
        list1 = input()
        a,b = list1.split(" ")
        a = int(a)
        b = int(b)
        print(a+b)
    except:
        break
    
