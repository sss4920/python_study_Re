a = int(input())
count = 0
while a!=0:
    if a==64:
        count+=1
        a-=64
    elif a<64 and a>=32:
        count+=1
        a-=32
    elif a<32 and a>=16:
        count+=1
        a-=16
    elif a<16 and a>=8:
        count+=1
        a-=8
    elif a<8 and a>=4:
        count+=1
        a-=4
    elif a<4 and a>=2:
        count+=1
        a-=2
    else:
        count+=1
        a-=1
print(count)
    
        
    
        
    
    
        
