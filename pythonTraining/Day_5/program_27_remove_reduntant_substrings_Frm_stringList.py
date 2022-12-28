a = input("Enter the value: ")
dup_items = set()
unique_items = []
for x in a:
    if x not in dup_items:
        unique_items.append(x)
        dup_items.add(x)
print(dup_items)
print(unique_items)
