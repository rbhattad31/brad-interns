n = 3
d = dict(input("Enter keys and Values").split() for _ in range(n))
"""
if "Ayush" in d.values():
    print("Correct")
else:
    print("Wrong")
"""
res=sorted(d.items())
print(res)

