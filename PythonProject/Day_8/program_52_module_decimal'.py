import decimal
x = float(input("Enter a Decimal Number"))
my_decimal = decimal.Decimal(x)
print(my_decimal)

import decimal
import math
a = decimal.Decimal(4.5).exp()
b = decimal.Decimal(2.5).sqrt()
c = decimal.Decimal(3.5).ln()
d = decimal.Decimal(1.5).log10()
print("The exponent of decimal number is : ", end="")
print(a)
print("The square root of decimal number is : ", end="")
print(b)
print("The ln of decimal number is : ", end="")
print(c)
print("The log10 of decimal number is : ", end="")
print(d)