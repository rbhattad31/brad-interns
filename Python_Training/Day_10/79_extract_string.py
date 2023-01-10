import re
a=input("Enter a string")
print(re.findall('"([^"]*)"', a))

