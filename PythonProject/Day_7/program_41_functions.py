def function_name():  # without parameters, without return
    print("Hello World")
function_name()

def sum_of_5_numbers(): # without parameters, with return
    sum = 0
    for i in range(1, 6):
        sum = sum + i
    return sum
x = sum_of_5_numbers()
print(x)

#def welcome_user(name, gender):  # with parameters, without return value
#    if gender == "M":
#        print("Welcome Mr.", name, ', Have a Nice Day ')
#    else:
#        print("Welcome Mrs.", name, ', Have a Nice Day ')
#name = input("Enter Your Name")
#
#gender = input("Enter Your Gender(M/F)")
#welcome_user(name, gender)

def get_count(arr, size, target_value):  # with parameters, with return value
    count = 0
    for i in range(0, size):
        if arr[i] == target_value:
            count = count + 1
    return count
my_list = [1, 1, 4, 1, 2, 4, 4, 3, 3, 4, 2, 1]
print("1 occurance : ", get_count(my_list, len(my_list), 1))
print("2 occurance : ", get_count(my_list, len(my_list), 2))
print("3 occurance : ", get_count(my_list, len(my_list), 3))
print("4 occurance : ", get_count(my_list, len(my_list), 4))
print(len(my_list))

def function(a, b, c):   # positional argument
    return b, a, c
print(function(1, 2, 3))

print(function(a=10, b=20, c=30))   # keyword arguments

def function(d=40, e=50, f=60):   # default arguments
    return d, e, f
print(function())
def vla(*args):  # variable length arguments
    return args  # prints in tuple
print(vla(1, 2, 3, 4, 5, 6, 7, 8, 9))
def ka(**kwargs):
    return kwargs
print(ka(g=1, h=2))  # print as a dictionary
