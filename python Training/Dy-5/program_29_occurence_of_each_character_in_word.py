test_str = "venkat in venkat"
res = {}
for keys in test_str:
    res[keys] = res.get(keys, 0)+1
print("count of all characters in venkat is :\n" + str(res))
