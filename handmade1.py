Test = int(input())             # 입력 받을 변수 만들기
for x in range(Test):           #입력 받은 변수 뭐시기만큼 for문 돌리기 2라고 입력 받으면 2번
    sum=0                       #합을 저장할 애
    a = map(int,input().split())#a라는 리스트에 1 2 3 4 5같은 애들을 받아
    for y in a:                 # a라는 리스트안에 요소들을 y에 각각 넣으며 반복 
        sum+=y                  # 합을 sum에 넣기
    print(sum)                  #반복문 나와서 sum을 출력
    
