import re


def isvalid(num):
    pattern = re.compile("^4[0-9]{12}(?:[0-9]{3})?$")
    return pattern.match(num)


num = input("enter the number:")
if isvalid(num):
    print("valid debit number")
else:
    print('invalid debit number')
