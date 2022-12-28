import copy
# Demonstrating the working of list.copy()
# Here we will create a list and then create a shallow copy using list.copy() in Python.
lis1 = [1, 2, 3, 4]

# Using copy() to create a shallow copy
lis2 = lis1.copy()

# Printing new list
print("The new list created is : " + str(lis2))

# Adding new element to new list
lis2.append(5)

# Printing lists after adding new element
# No change in old list
print("The new list after adding new element : \
" + str(lis2))
print("The old list after adding new element to new list  : \
" + str(lis1))
print()

# Demonstrating techniques of shallow and deep copy
# Here we will create a list and then create a shallow copy using list.copy() and deep Copy using deepcopy() in Python.


# Initializing list
list1 = [1, [2, 3], 4]

# all changes are reflected
list2 = list1

# shallow copy - changes to
# nested list is reflected,
# same as copy.copy(), slicing

list3 = list1.copy()

# deep copy - no change is reflected
list4 = copy.deepcopy(list1)

list1.append(5)
list1[1][1] = 999

print("list 1 after modification:\n", list1)
print("list 2 after modification:\n", list2)
print("list 3 after modification:\n", list3)
print("list 4 after modification:\n", list4)
