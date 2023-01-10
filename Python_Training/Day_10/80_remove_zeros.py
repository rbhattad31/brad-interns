import re
a=input("Enter Ip address")
b=[]
x=re.sub("\.[0]*",'.',a)
print(x)
