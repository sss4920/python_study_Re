def sum_digit(a):
    s=str(a)
    sum=0
    for x in s:
        x=int(x)
        sum += x
    return sum
print(sum_digit(1234))
