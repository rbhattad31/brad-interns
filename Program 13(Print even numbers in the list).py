num = [1, 2, 3, 4, 5, 20, 35, 38, 21, 65, 72]
print("This is the default list:", num)
even_num = []
for x in num:
    if x % 2 == 0:
        even_num.append(x)
print("Following is the list of even numbers:", even_num)