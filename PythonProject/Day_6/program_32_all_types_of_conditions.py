print("if condition")
a = 12
b = 12
if a == b:
    print("a is equals b")
print("if else condition")
c = 455
d = 487
if c<=d:
    print("c is greater than d")
else:
    print("d is greater than c")
print("if elif condition")
e = 45
f = 45
if e>f:
    print("e is greater than f ")
elif e==f:
    print("e is equals to f")
else:
    print("e is less than f")
print("nested if condition")
g = int(input("Enter a Number"))
if g>0:
    if g==0:
        print("zero")
    else:
       print("positive number")
else:
    print("negative number")
print("short hand if condition")
h = 5
i = 7
if i > h: print("i is greater than h")
print("short hand if else condition")
j = 4
k = 2
print("j") if j<k else print("k")
print("ternary condition")
c = 455
d = 487
print("c" if c<=d else "d")
