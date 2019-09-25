s = str(input().split())
if (s[-1] == " ")&(s[0] == " "):
    print(s.count(" ")-1)
elif s[-1] == " ":
    print(s.count(" "))
elif s[0] == " ":
    print(s.count(" "))
else:
    print(s.count(" ")+1)
