string_1 = input("Enter the string: ")
word = input("Enter world: ")
a = []
count = 0
a = string_1.split(" ")
for i in range(0, len(a)):
    if word == a[i]:
        count = count + 1
print("Count of the word is: ", count)
