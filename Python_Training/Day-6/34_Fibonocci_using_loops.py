n=int(input("Enter no of elements in series"))
n1=0
n2=1
if(n==0):
    print(n1)

elif(n==1):
    print(n2)


else:
    print(n1)
    print(n2)
    for i in range(3,n+1):
        res=n1+n2
        n1=n2
        n2=res
        print(res)





