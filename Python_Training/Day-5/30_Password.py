x=input("Enter Password")
a=b=c=d=0
for i in x:
    if(i.isdigit()):
        a+=1

    elif(i.islower()):
        b+=1

    elif(i.isupper()):
        c+=1

    elif(i=="@" or i=="#" or i=="$" or i=="_"):
        d+=1

if(a>=1 and b>=1 and c>=1 and d>=1):
    print("Valid Password")

else:
    print("Not Valid")
