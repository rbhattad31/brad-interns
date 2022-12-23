# Python code to demonstrate the working of
# sqrt() and exp()

# importing "decimal" module to use decimal functions
import decimal
import math

# sqrt() :- This function computes the square root of the decimal number.
# exp() :- This function returns the e^x (exponent) of the decimal number.
# using exp() to compute the exponent of decimal number
a = decimal.Decimal(4.5).exp()

# using sqrt() to compute the square root of decimal number
b = decimal.Decimal(4.5).sqrt()

# printing the exponent
print("The exponent of decimal number is : ", end="")
print(a)

# printing the square root
print("The square root of decimal number is : ", end="")
print(b)
print()

print(math.exp(65))
print(math.exp(-6.89))
print()

# ln() :- This function is used to compute natural logarithm of the decimal number.
# log10() :- This function is used to compute log(base 10) of a decimal number.
# using ln() to compute the natural log of decimal number
a = decimal.Decimal(4.5).ln()

# using sqrt() to compute the log10 of decimal number
b = decimal.Decimal(4.5).log10()

# printing the natural logarithm
print("The natural logarithm of decimal number is : ", end="")
print(a)

# printing the log10
print("The log(base 10) of decimal number is : ", end="")
print(b)
print()

# as_tuple()Returnsthedecimal number as tuple containing 3 arguments,sign(0 for +, 1 for -)digitsandexponentvalue
# ma(a,b) :- This “fma” stands for fused multiply and add. It computes (num*a)+b from the numbers in argument
# using as_tuple() to return decimal number as tuple
a = decimal.Decimal(-4.5).as_tuple()

# using fma() to compute fused multiply and addition
b = decimal.Decimal(5).fma(2, 3)

# printing the tuple
print("The tuple form of decimal number is : ", end="")
print(a)

# printing the fused multiple and addition
print("The fused multiply and addition of decimal number is : ", end="")
print(b)
print()

# copy_abs() :- This function prints the absolute value of decimal argument
# copy_negate() :- This function prints the negation of decimal argument
# copy_sign() :- This function prints the first argument by copying the sign from 2nd argument
# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(-9.56)

# printing absolute value using copy_abs()
print("The absolute value using copy_abs() is : ", end="")
print(b.copy_abs())

# printing negated value using copy_negate()
print("The negated value using copy_negate() is : ", end="")
print(b.copy_negate())

# printing sign effected value using copy_sign()
print("The sign effected value using copy_sign() is : ", end="")
print(a.copy_sign(b))