x = -245.425
print(abs(x))  # Return the absolute value of a number:

mylist = [True, True, True]  #  Check if all items in a list are True:
x = all(mylist)
print(x)

mylist = [False, False, False]  #  Check if any of the items in a list are True:
x = any(mylist)
print(x)

x = ascii("My name is Ståle")
print(x)
# The ascii() function will replace any non-ascii characters with escape characters: å will be replaced with \xe5.
# The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
x = bin(4)
print(x)  # The result will always have the prefix 0b

x = bytearray(4)
print(x)  #
x = compile('print(55)', 'test', 'eval')  # The_compile() function returns the specified source as a code object, ready to be executed.
exec(x)
def x():  #
  a = 5

print(callable(x))

