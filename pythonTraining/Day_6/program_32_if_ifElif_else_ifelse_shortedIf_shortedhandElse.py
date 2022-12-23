# if_statment
z = 4
if z % 2 == 0:
    print("Checking " + str(z))
    print("Even")
print()

# short_hand_if
a = 20
b = 10
if a > b: print("a is > b")
print()

#short_hand_if_else
a = 2
b = 330
print("A") if a > b else print("B")
print()

#ternary_operator
a, b = 10, 20
# copy value of a in min if a < b else copy b
minn = a if a < b else b
print(minn)
print()

#nested_if
num = 15
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive numbers")
else:
    print("Negative number")
print()