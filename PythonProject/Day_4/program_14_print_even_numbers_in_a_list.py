def even(list):
    new_list=[]
    for i in list:
        if i% 2==0:
            new_list.append(i)
    return new_list
list = []
n=int(input("Enter size of list "))
for i in range(0, n):
    list.append(i)

print("numbers in ", list)

# print(even(list))
