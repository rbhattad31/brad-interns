txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)
print()

print("------------")
y = x.casefold()
print(y)

print("------------")
z = txt.center(20, "O")
print(z)
print("------------")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "Hello, welcome to my world. "
x = txt.endswith("d")
print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(0)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.find("apple")
print(x)

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)

txt = "Hello, welcome to my world."
x = txt.index("to")
print(x)

txt = "Company12"   #
x = txt.isalnum()
print(x)

txt = "Company"  #
x = txt.isalpha()
print(x)
print("----------")
txt = "\u0033"  #
x = txt.isdecimal()
print(x)


