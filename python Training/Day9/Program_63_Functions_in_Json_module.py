import json

# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000,
     "married": True,
     "friendlessness's": None}

# conversion to JSON done by dumps() function
b = json.dumps(a)

# printing the output
print(b)
print(type(b))
x = '{ "name":"John", "age":30, "city":"New York","married":true}'

# parse x:
y = json.loads(x)
print(y)

# the result is a Python dictionary:
print(y["age"])
