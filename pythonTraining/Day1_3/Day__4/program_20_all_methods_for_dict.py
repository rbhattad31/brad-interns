# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# add elements to python dictionary
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ", capital_city)

# change value of dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)

student_id[112] = "Stan"

print("Updated Dictionary: ", student_id)

# Accessing Elements from Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters

# Removing elements from dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)

del student_id[111]

print("Updated Dictionary ", student_id)

# length of dict and clear
dict_1 = {'Name': 'steve', 'Age': 30, 'work': 'Programmer'}
print("Dictionary:", dict_1)
print("Length of dictionary:", len(dict_1))
print(dict_1.clear())
