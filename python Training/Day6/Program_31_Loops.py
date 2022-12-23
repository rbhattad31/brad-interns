# for_loop
for i in range(1, 11):
    print(i, end=" ")
# Break_in_for
print()
for val in range(1, 11):
    if val > 5:
        break
    print(val, end=" ")
# continue_in_for
print()
for val in range(1, 11):
    if val == 5:
        continue
    print(val, end=" ")
# pass_in_for
print()
for val in range(1, 11):
    pass
# While_loop
print("=" * 20)
i = 1
while i <= 10:
    print(i)
    i += 1
# Break_in_while.
print("=" * 20)
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print("=" * 20)
# Continue_in_while
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("=" * 20)
# pass_in_While
n = 5
while n > 0:
    pass
