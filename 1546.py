n = int(input())
sum1 = 0
score = input().split(" ") ##
score = list(map(float,score))
max_score = 0
for x in range(n):
    if max_score < score[x]:
        max_score = score[x]
for x in range(n):
    score[x]=score[x]/max_score
print((sum(score)/n)*100)
