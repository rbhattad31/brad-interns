# assertion error
try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)

# the error_message provided by the user gets printed
except AssertionError as msg:
    print(msg)
print("****************************************************")
# EOFError
n = int(input())
print(n * 10)


try:
    n = int(input())
    print(n * 10)

except EOFError as e:
    print(e)
print("*********************************************************")
# attribute error
class main():

    def __init__(self):
        self.a = 'hello python'


# Driver's code
obj = main()

print(obj.a)

# Raises an AttributeError as there
# is no attribute b
print(obj.b)
# floating point error
import math

print(math.exp(1000))


# 2nd type
import sys
import math
import fpectl
try:
    print ('Control off:', math.exp(700))
fpectl.turnon_sigfpe()
print ('Control on:', math.exp(1000))
except Exception as e:
print(e)
print (sys.exc_type)