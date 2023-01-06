import re
a=input("Enter a password")
x=re.findall("\d",a)
y=re.findall("[a-zA-Z]",a)
z=re.search("@",a)
if(x and y and z):
    print("Valid Password")
else:
    print("Not a Valid Password")
