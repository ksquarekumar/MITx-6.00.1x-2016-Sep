

s= raw_input('Enter String',) # s already defined


def vowelcount(s):
    n=0
    for i in s:
        if (i == 'a' or i == 'e' or i == 'o' or i=='i' or i =='u'):
            n+=1

    return n

print vowelcount(s)
