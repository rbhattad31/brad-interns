A = [2, 5, 19, 7, 43]

print("Length of string is", len(A))
print("Maximum number in list is ", max(A))
print("Type is", type(A))
print("***********************")
# calling a function


def fun():
    print("welcome to python")


fun()
print("**************************")
# default argument


def myfun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myfun(10)
print("**************************")
# keyword argument


def student(firstname, lastname):
    print(firstname, lastname)


student(firstname='siva', lastname='kumar')
student(lastname='kumar', firstname='siva')
print("**************************")
# variable_length argument
# for non-keyword


def myfun(*argv):
    for arg in argv:
        print(arg)


myfun('Hello', 'Welcome', 'to', 'python')
print("******************************")
# for length key argument


def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myfun(first='venkat', mid='durga', last='prasad')
print("*************************************")
# mixed function


def displayarguments(argument1, *argument2, **argument3):
    print(argument1)

    # displaying non keyword arguments
    for arg in argument2:
        print(arg)

    # displaying non keyword arguments
    for arg in argument3.items():
        print(arg)


arg1 = "Welcome"
arg3 = "To"

displayarguments(arg1, "to", arg3, agr4=4, arg5="python !")
print("**********************************")