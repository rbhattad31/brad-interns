Normal_list = [1, 3, 4, 2, 1, 2, 3, 4, 5, 6, 5, 6, 7, 6, 7, ]
Unique_list = []
for i in Normal_list:
    if i not in Unique_list:
        Unique_list.append(i)
print(Unique_list)