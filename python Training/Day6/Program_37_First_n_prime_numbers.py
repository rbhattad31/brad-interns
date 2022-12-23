lower = int(input("enter lower interval :"))
upper = int(input("enter upper interval :"))
print("first n prime numbers are:")
for n in range(lower, upper + 1):
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end="  ")
