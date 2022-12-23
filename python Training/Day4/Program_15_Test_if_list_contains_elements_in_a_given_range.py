a = [4, 2, 5, 6, 7, 3, 9]
print("Original list is : " + str(a))
i, j = 2, 10
res = True
for e in a:
    print(e)
    if e < i or e >= j:
        print(e)
        res = False
        break
print("Does list contain all elements in range : " + str(res))

