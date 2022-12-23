a = input("enter value of a : ")
b = input("enter value of b : ")
print("original value of a is {}".format(a))
print("original value of b is {}".format(b))
a, b = b, a
print("swapped value of a is {}".format(a))
print("swapped value of b is {}".format(b))
