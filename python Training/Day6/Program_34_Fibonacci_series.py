print("=" * 20)
n = int(input("enter value of n:"))
a = 0
b = 1
sum = 0
count = 1
print("fibonacci series is: ")
while count <= n:
    print(sum)
    count += 1
    a = b
    b = sum
    sum = a + b
print("=" * 20)
