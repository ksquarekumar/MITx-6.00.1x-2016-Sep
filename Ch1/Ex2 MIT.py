

s= raw_input('Enter String',) # s already defined


def subcount(s):
    n=0
    for i in range(0,len(s),1):
        if s[i:i+3]=="bob":
            n+=1

    return n

print subcount(s)
