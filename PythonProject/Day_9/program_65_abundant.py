def is_abundant(n):
    fac_sum = sum([fac for fac in range(1, n) if n% fac == 0])
    return fac_sum > n
a = int(input("enter the number"))
if is_abundant(a):
    print("The number is abundant")
else:
    print("the number is not a abundant")
