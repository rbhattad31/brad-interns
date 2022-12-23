# if statement
num = 10
if num > 0:
    print("number is positive")
print("The if statement is easy")
print("********************************")
# 'if... else...' statement
number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')
print('This statement is always executed')
print("****************************")
# 'if...elif...else..'
number = 0
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')
print('This statement is always executed')
print("*******************")
# 'Nested if'
number = 5
if number >= 0:                  # outer if statement
    if number == 0:                # inner if statement
        print('Number is 0')       # inner else statement
    else:                          # inner else statement
        print('Number is positive')
else:                              # outer else statement
    print('Number is negative')
print("**********************")
# 'shorthand if'
a = 200
b = 33
if a > b: print("a is greater than b")
print("************************")
# 'shorthand if else'
a = 2
b = 330
print("A") if a > b else print("B")
print("****************************")
# Ternary operator
a, b = 10, 20
minimum = a if a < b else b
print(minimum)
