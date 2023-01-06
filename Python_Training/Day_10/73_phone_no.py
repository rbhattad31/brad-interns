import re
a=input("Enter a number")
x=re.findall("[0-9]",a)
y=re.findall("[a-n]",a)
if(x and not y):
    print("Phone number is valid")

else:
    print("Please enter a valid phone no")

