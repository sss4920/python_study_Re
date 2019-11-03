di={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
s=input()
number=0
for x in s:#문자열 하나하나
    for y in range(len(di)):#딕셔너리 크기만큼
        if x in di[y+2]:
            number+=y+2
            break
print(number+len(s))
        
