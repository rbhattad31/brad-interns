fruits = ["apple", "banana", "cherry"]  # for loop
for x in fruits:
  print(x)
print("---------")
i = 1  # while loop
while i < 10:
    print(i)
    i += 1
print("---------")
print("break statement")
i=1
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1
print("continue statement")
i=1
while i<10:
    i += 1

    if i == 4:

        continue
    else:
        print(i)
