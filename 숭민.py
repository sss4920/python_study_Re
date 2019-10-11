def num_vowel(f):
    a=0
    for i in f:
        if i in 'aeiou':
            a+=1
    print(a)
b = input()    
num_vowel(b)
