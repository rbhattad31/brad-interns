import math
a=int(input("Enter a number"))
n=int(input("Enter power"))

temp=a
result=0
while(a>0):
    rem=a%10
    result=result+(math.pow(rem,n))
    a=a//10

if(result==temp):
    print("It is an Armstrong Number")

else:
    print("Not an Armstrong Number")

