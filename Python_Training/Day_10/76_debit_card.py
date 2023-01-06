import re
a=input("Enter your debit card no")
x=re.findall("^4",a)
y=re.findall("^5",a)
z=re.findall("^6",a)
b=re.findall("[0-9]",a)
if((x or y or z) and b and len(a)==16):
    print("Correct")
else:
    print("Not valid")
