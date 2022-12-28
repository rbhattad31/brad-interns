# append_method
list_of_one = ['Mathematics', 'chemistry', 'Hello', 'World']
list_of_one.append(20445)
print(list_of_one)

# insert_method
list_of_one.insert(45, 98)
print(list_of_one)

# extend_method
a = list_of_one
b = [1, 2, 3, 4, 5]
a.extend(b)
print(a)
b.extend(a)
print(b)

# sum_of_list
c = [1, 2, 3, 4, 5, 6]
print(sum(c))

# count_of_list
d = c
print(d.count(6))

# length_of_list
print(len(d))

# index_of_list
print(d.index(4))

# print_index_after_n_no_of_values
print(d.index(3, 2))

# pop()
list_of_pop = [1, 2, 3, 4, 5, ]
print(list_of_pop.pop())

# del() and remove
list_of_del = [11, 22, 33, 44, 55, 66, 77, 88, ]
del list_of_del[0]
print(list_of_del)
list_of_del.remove(22)
print(list_of_del)














