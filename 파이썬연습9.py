h,m = input().split(" ")
h = int(h)
m = int(m)
if h == 0:
    if m >= 45:
        m -= 45
        print(h,m)
    else:
        diff =45 - m
        m = 60-diff
        h = 23
        print(h, m)
else:
    if m >= 45:
        m -= 45
        print(h,m)
    else:
        diff =45 - m
        m = 60-diff
        h -= 1
        print(h, m)
