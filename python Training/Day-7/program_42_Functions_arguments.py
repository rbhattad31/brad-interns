# pass by reference
def set_list(n):
    n = ["A", "B", "C"]
    return n


def add(n):
    n.append("D")
    return n


my_list = ["E"]

print(set_list(my_list))

print(add(my_list))
print("*******************************")
# anonymous function
k = lambda a, b, c: a+b+c
s = k(12, 24, 56)
print(s)
print("************************************")
# function in function


def f1():
    s = 'I love python'

    def f2():
        print(s)

    f2()


f1()
