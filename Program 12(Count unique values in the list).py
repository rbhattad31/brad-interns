new_list = [1, 2, 3, 4, 5, 5, 4, 2, 1, 2, 4, 6, 7, 2, 3, 4, 5, 6 ]
empty_list = []
count = 0

for i in new_list:
    if i not in empty_list:
        count += 1
        empty_list.append(i)

print("No of unique values in the given list is:", count)
