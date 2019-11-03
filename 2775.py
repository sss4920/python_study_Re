test = int(input())
for x in range(test):
    floor = int(input())
    ho = int(input())
    first = []
    for y in range(floor+1): #floor는 0부터 1까지 움직여
        hoho=[]
        for hosil in range(1,ho+1): #hosil은 1부터 3호까지 움직여
            hoho.append(1)
                      
        first.append(hoho)
    print(first)
