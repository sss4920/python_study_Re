number = int(input())
com = [0]
sum1=1
j=2 
k=j-2 #방번호
a=list(map(int,input().split()))
temp1=0 # 제곱수 임시저장 변수
for x in a: #약수 2,3,4,6이라는 케이스가 있다고 치자
    i=2 #계속 나눠줄 변수 i선언
    while x!=1: # 약수가 완전히 나누어떨어질때까지 반복
        k=i-2
        if x %i == 0: # i가 2일때 나누어 떨어지면
            x=x//i # 나눈몫을 넣고
            temp1+=1 # 그 제곱수를 센다    
            if i==k+2 and com[k]<temp1: #만약에 그 제곱수가 기존 제곱수보다 크면
                com[k]=temp1 #2의 제곱수를 배열의 첫번째에 저장
                temp1=0
        else:
            i+=1
            temp1=0
            com.append(0)
            
for y in range(len(com)):
    if com[y] ==0:
        j+=1
        continue
    sum1*=j**com[x]
    j+=1
print(sum1)

            
        
        
    
    
