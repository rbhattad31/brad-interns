my_list = []
num = int(input("Enter no of elements:"))
for i in range(0,num):
    elements = int(input("Enter the element:"))
    my_list.append(elements)

x = int(input("Enter the min value of the range:"))
y = int(input("Enter the max value of the range:"))

for items in my_list:
    if(items >= x and items <= y):
        print("Elements are in range")
        break

    else:
        print("Elements not in range")
        break