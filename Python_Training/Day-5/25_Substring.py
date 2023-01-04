a=input("Enter a word")
print([*a])

l=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            l.append(i)
            l.append(j)
            break

print(l)





