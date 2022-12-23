list = ["Apple", "Banana", "cherry", "Orange", "Kiwi", "Melon", "Mango"]
print(list)
print("-------")

print(len(list))

print("-------")
print(type(list))
print(type(9))
print(type('9'))
print("-------")
print(list[0])

print("-------")
print(list[-1])  # Negative indexing means starting from the end of the list.
print("-------")
print(list[2:6])
print("-------")
print(list[:4])  # remember that the item in index 4 is not included
print("-------")
print(list[2:])  # this will return the items from index 2 to end.
print("-------")
print(list[-3:-1])   # Negative indexing means starting from the end of the list.
print("-------")
list[1] = "blackcurrant"  # replace the item
print(list)
print("-------")

list.append("orange")  # append
print(list)
print("-------")
list.insert(1, "orange")   # insert
print(list)
print("-------")
mylist = ["apple", "banana", "cherry"]    # extend
list1 = ("kiwi", "orange")
mylist.extend(list1)
print(mylist)
print("-------")
list = ["apple", "banana", "cherry"]  # remove
list.remove("banana")
print(list)
print("-------")
list = ["apple", "banana", "cherry"]  # Remove Specified Index
list.pop(1)
print(list)
print("-------")
list = ["apple", "banana", "cherry"]   # clear the list
list.clear()
print(list)
print("-------")
list = ["apple", "banana", "cherry"]  # print the list one by one
for x in list:
    print(x)
print("-------")


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


newlist = []
for x in fruits:
    if "p" in x:
     newlist.append(x)
print(newlist)
print("-------")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]  # sort
thislist.sort()
print(thislist)
print("-------")
thislist = [100, 50, 65, 82, 23]   # sort the list numerically
thislist.sort()
print(thislist)
thislist.sort(reverse=True)  # sort the list descending
print(thislist)

print("---")
list = fruits.copy()

print(list)
print("-------")
list = fruits.count("cherry")
print(list)
print("-------")
x = fruits.index("cherry")
print(x)
print("-------")
fruits.pop(2)
print(fruits)
print("-------")
