dict1 = {"Name": "shiva",
        "Age": "24",
        "study": "MTech"}
dict2 = {"Coarse": "Mech"}
dict3 = {**dict1, **dict2}
print(dict3)
print(len(dict3))
