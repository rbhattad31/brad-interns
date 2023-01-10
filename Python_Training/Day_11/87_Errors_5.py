"""
print("Program that uses SystemExit as Exception instead of BaseException.")
try:
    raise SystemExit

except SystemExit:
    print("Specifying SystemError exception in this block works.")
"""
"""
try:
    a=input("Enter a string")
    b=int(input("Enter a number"))
    c=a+b
except:
    print("TypeError")

else:
    print(c)
"""
"""
try:
    print(a)
    a=6
except:
    print("UnboundLocalError")
"""
"""
try:
    a = u'éducba'
    b = a.encode('utf8')
    unicode(b)
except:
    print("UniCode Error")
"""

