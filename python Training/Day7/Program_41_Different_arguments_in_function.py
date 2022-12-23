# Non default arguments
def add(a, b, c):
    d = a + b + c
    print(d)


add(10, 20, 30)


# Default arguments
def sub(a=30, b=20):
    c = a - b
    print(c)


sub()


# Non keyword arguments
def display(empnum, sal):
    print("Employee Number", empnum)
    print("Employee sala", sal)


display(1, 8000)


# length of arguments
def show(*a):
    print(a)
    print(type(a))


show(34, 53)
print()


def show(**c):
    print(c)
    print(type(c))


show(a=100, b=200)
