import sys

print(sys.version)
sys.stdout.write('Geeks')
print(end=" ")
age = int(input("enter any number:"))

if age < 18:

    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
