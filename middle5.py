a=input("단어입력:")
print("입력 받은 단어:%s"%a)
b=[]
c=""
for x in a:
    b.append(ord(x))
b=set(b)
b=list(b)
b.sort()
for x in b:
    c+=chr(x)
print("단어에 포함된 알파벳:%s"%c)
