

s= input('Enter String',) # s already defined

mains  = ["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

s =s+str(0)
cc =0
cl =0
sc = ""
slarge = ""


for i in range(0,len(s),1):
    for j in range(0, len(mains), 1):
        if(s[i]==mains[j]):
            if (j<cc):
                cl = cc
                if(len(sc)>len(slarge)):
                    slarge = sc
                sc = ""
            cc = j
            sc = sc + s[i]
print (slarge)
#print snew[0]