# Import math Library
import math

# Print the value of pi
print (math.pi)
print()

# radius of the circle
r = 4

# value of pie
pie = math.pi

# area of the circle
print(pie * r * r)
print()

# Tau is defined as the ratio of the circumference to the radius of a circle.
# The math.tau constant returns the value tau:
# 6.283185307179586.
# Import math Library

# Print the value of tau
print(math.tau)
print()
# Print the positive infinity
print(math.inf)

# Print the negative infinity
print(-math.inf)

# The math.nan constant returns a floating-point nan (Not a Number) value.
# This value is not a legal number.
# The nan constant is equivalent to float(“nan”).
# Print the value of nan
print(math.nan)
print()

a = 5

# returning the factorial of 5
print("The factorial of 5 is : ", end="")
print(math.factorial(a))
print()

a = 15
b = 5

# returning the gcd of 15 and 5
print("The gcd of 5 and 15 is : ", end="")
print(math.gcd(b, a))
print()

# fabs() function returns the absolute value of the number.
a = -10

# returning the absolute value.
print("The absolute value of -10 is : ", end="")
print(math.fabs(a))
print()

test_int = 4
test_neg_int = -3
test_float = 0.00

# checking exp() values
# with different numbers
print(math.exp(test_int))
print(math.exp(test_neg_int))
print(math.exp(test_float))
print()


