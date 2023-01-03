print("Program to demonstrate to handle ImportError:")
print("\n")
try:
 from crypt import pwd
except ImportError as ie:
 print("It cannot import module and submodule", ie)
print("______________________________________________________________________")

list = [1, 4, 5, 78, 454, 46564]
try:
    print(list[6])
except IndexError as ier:
    print(ier)
print("______________________________________________________________________")

ages = {'ramesh': 30, 'Ram': 28, 'raju': 33}
person = input('Get age for: ')
age = ages.get(person)
try:
    print(f'{person} is {age} years old')
except KeyError as ke:
    print(f'{person} age is unknown')
print("______________________________________________________________________")


try:
    str_name = input('Enter the name of the user ')
except KeyboardInterrupt:
    print('Hello user you have pressed ctrl-c button.')
else:
    print('Hello user there is some format error')
