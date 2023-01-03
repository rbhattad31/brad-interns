try:
    x = 1                #  float(input("Enter a number"))
    y = 0               #  float(input("Enter a number"))
    assert y != 0, "invalid operation"
    print(x / y)
except AssertionError as meg:
    print(meg)
i = 1
try:
    i.append(4)
except AttributeError:
    print("No Attributes")
try:
    num = 0             # float(input("Enter a number"))
    print(num*10)
except EOFError as er:
    print(er)
