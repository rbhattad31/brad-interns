#We will calculate area using Heron's Formula
import math
a=int(input("Enter Side a"))
b=int(input("Enter Side b"))
c=int(input("Enter Side c"))
s=(a+b+c)/2
if(a<=0 & b<=0 & c<=0):
    print("Invalid input Given")
else:
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(area)
