#value
"""
try:
    def func(a,b):
        c=a+b
        return c
    print(func(5,'Ayush'))
except:
    print("ValueError")
"""
#zero error
try:
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    c=a/b
except:
    print("ZeroDivisionError")
else:
    print(c)
