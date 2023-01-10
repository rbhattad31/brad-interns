"""
a=int(input("Enter a number"))
if(a%2!=0):
    raise Exception("Only Even Numbers allowed")
else:
    print("Ok Satisfied")
"""
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=a/b
if(b==0):
    raise ZeroDivisionError("Cannot Divide by zero")
else:
    print(c)