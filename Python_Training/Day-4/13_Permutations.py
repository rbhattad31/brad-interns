a=int(input("Enter the number"))
b=[int(x) for x in str(a)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(b[i]!=b[j]& b[j]!=b[k] & b[k]!=b[i]):
                print(b[i],b[j],b[k])

