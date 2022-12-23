print("=" * 20)
n = int(input("enter any number:"))
s = n
b = len(str(n))
sum = 0
while n != 0:
    r = n % 10
    sum = sum + (r ** b)
    n = n // 10
if s == sum:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
