#assertion
"""
try:
    a=int(input("Enter a number"))
    assert a>0
except:
    print("Error-Please enter a positive number")

else:
    print(a)
"""
#attribute
"""
try:
    a=int(input("Enter a number"))
    a.append(5)
except:
    print("No such Attribute")
"""
#eof
"""
try:
    a=int(input("Enter"))
    print(a * 10)

except:
    print("EOF Error")
"""
#floatingpoint
try:
    a=int(input("Enter a number"))
    b=a/0
except:
    print("Floating Point error")
