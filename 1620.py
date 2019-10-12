import sys
a,b =map(int,sys.stdin.readline().split())
poketmon=[]
for x in range(a):
    c = sys.stdin.readline().rstrip()
    poketmon.append(c)
for y in range(b):
    sen = sys.stdin.readline().rstrip()
    if sen.isalpha():
        if sen in poketmon:
            print((poketmon.index(sen))+1)
    elif sen.isdigit():
        sen=int(sen)
        print(poketmon[sen-1])
