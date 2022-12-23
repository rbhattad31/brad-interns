a = [1, 2, 3, 4]  # pass by reference
def hello(x):
    x[0] = 5
    print(x)
    return
hello(a)
print(a)


def Hello(x):      #  pass by value
    x = 55
    print(x)
    return
x = 15
Hello(x)
print(x)

str1 = 'Hello India'  # anonymous function or lambda function
# lambda returns a function object
rev_upper = lambda string: string.upper()[::1]
print(rev_upper(str1))

def outer_func(name):
    name = "Someone"
    def inner_func():
      print(name)
    inner_func()
outer_func("")
