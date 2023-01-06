import re
a=input("Enter Email-ID")
x=re.findall("@gmail.com",a)
y=re.findall("@yahoo.com",a)
z=re.findall("outlook.com",a)
b=re.findall("hotmail.com",a)
if(x or y or z or b):
    print("Email Entered is Valid")
else:
    print("Please enter a valid Email-id")
