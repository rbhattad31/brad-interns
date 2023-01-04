def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n or (sum/2)==n):
        print("Perfect Number")
    else:
        print("Not a perfect Number")



perfect(8128)
