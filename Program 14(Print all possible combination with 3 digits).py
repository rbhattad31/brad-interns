numbers_list = []
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

numbers_list.append(num1)
numbers_list.append(num2)
numbers_list.append(num3)

for x in range(0, 3):
    for y in range(0, 3):
        for z in range(0, 3):

            if ( x != y, y != z, z != x ):
                print(numbers_list[x], numbers_list[y], numbers_list[z])
