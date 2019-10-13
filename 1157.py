a = input()# 문장 받음
b=[]
for x in range(32):
    b.append(0)
for x in a:# 문장의 길이만큼 반복
    i=65
    for y in range(32):
        if (ord(x)== i) or (ord(x)==i+32):#대문자든 소문자든
            b[i-65]+=1
            break
        else:
            i+=1
maxi = max(b)
count1 = b.count(maxi)
if count1 >1:
    print('?')
elif count1==1:
    mini= chr(65+b.index(max(b)))
    print(mini)
    
    
