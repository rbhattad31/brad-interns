test = ["Welcome to python", "Core python", "Advanced python"]
K = "python"
print("The original list : ", test)
res = []
for i in range(0, len(test)):
    if test[i].find(K) != -1:
        res.append(i)
print("The indices list : ", res)
