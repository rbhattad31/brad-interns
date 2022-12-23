# shallow copy
l1 = [1, 2, 45, 67, 34, 90, "banana", "apple"]
l2 = l1.copy()
print(l1, id(l1))
print(l2, id(l2))
# deep copy
l3 = [23, 56, 23, 89, 45]
l4 = l3
print(l3, id(l3))
print(l4, id(l4))
l3.append(51)
l4.append(89)
print(l3)
print(l4)
l1.append(43)
l2.append(67)
print(l1)
print(l2)
