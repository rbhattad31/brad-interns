a = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: {6: "Seven"}}
print("The dictionary before changing the value is:", a)
a[5][6] = "Six"
print("The dictionary after changing the value is:", a)