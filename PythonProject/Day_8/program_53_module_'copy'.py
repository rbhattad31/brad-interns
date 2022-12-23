import copy
list1 = [11, [12, 13], 14]
list2 = list1
list3 = list1.copy()
list4 = copy.deepcopy(list1)
list1.append(15)
list1[1][1] = 99
print("list 1 after modification:\n", list1)
print("list 2 after modification:\n", list2)
print("list 3 after modification:\n", list3)
print("list 4 after modification:\n", list4)
