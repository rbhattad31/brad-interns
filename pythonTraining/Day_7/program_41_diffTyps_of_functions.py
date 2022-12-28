# built_in_functions
# length,list,max,min,open,print,str,sum,type,tuple
length_of_str = "string"
print(len(length_of_str))
print()

print(list(length_of_str))
print()

print(max(length_of_str))
print()

print(min(length_of_str))
print()

number = 4
print(type(number))
print(type(str(number)))
print()

sum_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(sum_of_numbers))
print()

print(tuple(sum_of_numbers))
print()
# user_difined_functions
x_1 = 3
x_2 = 4


def add():
    print(x_1+x_2)


add()


print()


def fun():
    print("Welcome to Python")


fun()

print()

# Arguments of a python


def evenodd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("odd")


evenodd(2)
evenodd(3)


# Python program to demonstrate
# default arguments


def myfun(x, y=50):
    print("x: ", x)

    print("y: ", y)


# Driver code (We call myFun() with only
# argument)

myfun(10)


# Python program to demonstrate Keyword Arguments

def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments

student(firstname='Hemanth', lastname='kumar')

student(lastname='kumar', firstname='Hemanth')
