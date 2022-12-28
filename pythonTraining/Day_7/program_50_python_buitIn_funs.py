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

# for integers
print(round(15))
print()
# for floating point
print(round(51.6))
print(round(51.5))
print(round(51.4))
print()

# Python program to illustrate
# built-in method bool()

# Returns False as x is False
x = False
print(bool(x))

# Returns True as x is True
x = True
print(bool(x))

# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x == y))

# Returns False as x is None
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

# Returns False as x is an empty mapping
x = {}
print(bool(x))

# Returns False as x is 0
x = 0.0
print(bool(x))
print()
print()


# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
print()

# print first 5 integers
# using python range() function
for i in range(5):
    print(i, end=" ")
print()
print()

String = 'Hello World'
slice_obj = slice(5,11)
print(String[slice_obj])
print()

print(sorted([4, 1, 3, 2]))
print()
x = ord("h")
print(x)
print()