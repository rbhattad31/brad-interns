"""
try:
    a=[]
    for i in range(1000000):
        for j in range(100000000):
            a.append("More")
except:
    print("Out of memory")
else:
    print(a)
"""
