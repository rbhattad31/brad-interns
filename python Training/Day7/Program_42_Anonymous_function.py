# pass reference
def myfunction(arg):
    print("list received {} has id {}".format(arg, id(arg)))
    arg.append(40)
    print("list changed {} has id {}".format(arg, id(arg)))


x = [10, 20, 30]
print("list sent {} has id {}".format(x, id(x)))
myfunction(x)
print("list after function call {} has id {}".format(x, id(x)))


def main():
    n = 9001
    print(f"Initial address of n: {id(n)}")
    increment(n)
    print(f"  Final address of n: {id(n)}")


def increment(y):
    print(f"Initial address of x: {id(y)}")
    y += 1
    print(f"  Final address of x: {id(y)}")


main()
# Lambda function
k = lambda a, b, c: a + b + c
s = k(12, 34, 56)
print(s)


# Function in function
def outer_func():
    def inner_func():
        print("Hello, World!")

    inner_func()


outer_func()
