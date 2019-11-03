di={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
s = input()
for x in range(len(s)):#문자열 한글자씩 뽑아서
    for y in range(len(di)):#딕셔너리랑 비교
        if di[y] == s[x]:#딕셔너리랑 value가 같으면 그 문자를 인덱스로 바꿔
            di[y]= x
            break
for x in range(len(di)):
    try:    
        if di[x].isalpha():
            di[x]=-1
    except:
        pass
for x in range(len(di)):
    print(di[x],end=" ")
        
                
