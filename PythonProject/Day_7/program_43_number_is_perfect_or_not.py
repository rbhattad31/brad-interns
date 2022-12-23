def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(496))
print(perfect_number(8128))

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if n % i == 0:
        sum1 = sum1 + i
if sum1 == n:
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
