n,m = input().split()
n = int(n)
m=int(m)
card = map(int,input().split())
card = list(card)
card.sort()
sumcard = 0
i = 0
j=0
k=0
sumlist=[]
while True:
    while i < len(card)-4:
        while j < len(card)-3:
            while k < len(card)-2:
                sumcard =card[i]+card[j+1]+card[k+2]
                sumlist.append(sumcard)
                k+=1
            k=1    
            j+=1
        k=2
        j=1
        i+=1
    break
for x in len(sumlist):
    if m < sumlist[x]:
        print(sumlist[x-1])
        break
        
    

    
