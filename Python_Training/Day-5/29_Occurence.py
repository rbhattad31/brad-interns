a=input("Enter a word")
l={}
for i in a:
    if i in l:
        l[i]=l[i]+1

    else:
        l[i]=1

print(str(l))


