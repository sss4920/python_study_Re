sum1=0
def sum_list(x):
    sum1=0
    for i in range(len(x)):
        sum1+=x[i]
    return sum1
li=[1,2,3,4,5]
result=sum_list(li)
print(result) 
