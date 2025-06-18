Str=input("Enter the dna bases : ").upper()
a=0
t=0
c=0
g=0
for  i in range(len(Str)):
    if Str[i] == 'A':
        a+= 1
    elif Str[i] == 'T':
        t+= 1
    elif Str[i] == 'C':
        c+= 1
    elif Str[i] == 'G':
        g+= 1
dict={"A":a,"T":t,"C":c,"G":g}
print(dict)