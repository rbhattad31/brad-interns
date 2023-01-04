n = 3
d = dict(input("Enter keys and Values").split() for _ in range(n))
a=[x for x in d.items()]
a.sort()
print(a)






