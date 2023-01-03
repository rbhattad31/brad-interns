import re

passwd = input("Enter the password")
regular = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
pattern = re.compile(regular)
print(pattern)

    # searching regex
mat = re.search(pattern, passwd)
print(mat)
print(type(mat))
    # validating conditions
if mat:
    print("Password is valid.")
else:
    print("Password invalid !")



