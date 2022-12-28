# while_loop
counter = 0
while counter < 3:
    counter = counter + 1
    print("Hello world")
print()

# while_&_else
counter_1 = 0
while counter_1 < 3:
    counter_1 = counter_1 + 1
    print("Hello counter")
else:
    print("In else block")
print()

# FOR_LOOP
num = 4
for i in range(0, num):
    print(i)

print()

# for_loop_by_iterating_by_index
list_of_one = ["hemanth", "Python", "JavaScript"]
for index_of in range(len(list_of_one)):
    print(list[index_of])
print()
list_of = ["Hello", "Hi", "word"]
for index in range(len(list_of)):
    print(list_of[index])
else:
    print("Inside Else Block")
print()

# nested_for_loop
x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)
print()

# continue_in_loops
for letter in 'Hemanthkumar':
    if letter == 'e' or letter == 'H':
        continue
    print("Current letter :", letter)
print()
# break_in_loops

for letter in "Helloworld":
    if letter == 'e' or letter == 'H':
        break

print(letter)
print()

# pass_in_loops
for letter in "HelloHemanth":
    pass
print(letter)
print()

# A_SIMPLE_LOOP_EXAMPLE
fruits = ['apple', 'Mango', 'Orange']
for fruit in fruits:
    print(fruit)
print()

# if_statment
apple = 33
mango = 200
if apple < mango:
    print('True')
print()

# using_if_elif_else
a = 300
b = 22
if b > a:
    print("b is > a")
elif a == b:
    print("a and b are ==")
else :
    print("a is > b")
print()

# pass_statment
aa = 33
bb = 44

if bb > a:
    pass
