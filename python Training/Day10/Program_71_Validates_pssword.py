import re

password = input("enter the password:")
print(password)
if len(password) < 8:
    print("password must be 8 characters long")
if not re.search('[A-Z]', password):
    print("not valid,password must contain atleast one capital letter")
if not re.search('[a-z]', password):
    print("not valid,password must contain atleast one small letter")
if not re.search('[0-9]', password):
    print("not valid,password must contain atleast one digit")
if re.search('\s', password):
    print("not valid,password should not contain white space")
if not re.search('[!@#$%&_+]', password):
    print("not valid,password should contain atleast one special symbol")
else:
    print("password is correct")
