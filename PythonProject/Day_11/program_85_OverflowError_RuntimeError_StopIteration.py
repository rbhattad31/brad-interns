

j = float(input("Enter Number"))

try:
    for i in range(1, 1000):
        j = j**i
        print(j)
except OverflowError as ofe:
    print("Overflow error happened")
    print(f"{ofe}, {ofe.__class__}")

print("==============================================================================================================")
a = 1
b = "1"
print(int(15.1))
print(a+b)
print("==============================================================================================================")
# try:
#    open("database.sqlite")
# except OSError:
#    raise RuntimeError("unable to handle error")

