# append-adding element to the list
List = ['Mathematics', 'chemistry', 1997, 2000]
List.append(20544)
print(List)
# insert-an element at the specified position
List.insert(3, 1456)
print(List)
# extend-Adds contents to List2 to the end of List1
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
List1.extend(List2)
print(List1)
List2.extend(List1)
print(List2)
# add - Calculates the add of all the elements of the List
Num = [1, 2, 3, 4, 5]
print(sum(Num))
# count-Calculates total occurrence of a given element of List
list1 = [1, 2, 1, 5, 4, 6, 2, 3, 1, 8, 1, 1, 7, 1]
print(list1.count(1))
# length-Calculates the total length of the List
list2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(len(list2))
# index-Returns the index of the first occurrence. The start and End index are not necessary parameters
list3 = [12, 15, 16, 17, 19]
print(list3.index(15))
# copy-it returns a shallow copy of a list
my_list = ['cat', 0, 6.7]
new_list = my_list.copy()
print("copied list:", new_list)
# clear-removing all elements from the list
numbers = [2, 3, 4, 5, 9, 7, 1, 5]
numbers.clear()
print('list after clear:', numbers)
# remove-removes a given object from the list
numbers = [2, 3, 4, 5, 9, 7, 1, 5]
numbers.remove(9)
print('updated list:', numbers)
# reverse-reverse objects from the list
numbers = [2, 3, 4, 5, 9, 7, 1]
numbers.reverse()
print('reversed list:', numbers)
