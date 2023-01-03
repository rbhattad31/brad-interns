# It should be 13 or 16 digits long, new cards have 16 digits and old cards have 13 digits.
# It should start with 4.
# If the cards have 13 digits the next twelve digits should be any number between 0-9.
# If the cards have 16 digits the next fifteen digits should be any number between 0-9.
# It should not contain any alphabet or special characters.
# Card number using regular expression
import re

def isValidVisaCardNo(string):
    # Regex to check valid Visa Card number
    regex = "^4[0-9]{12}(?:[0-9]{3})?$"

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if string == '':
        return False

    m = re.match(p, string)

    if m is None:
        return False
    else:
        return True


# Driver code
if __name__ == "__main__":
    # Test Case 1
    str1 = "4155279860457"
    print(isValidVisaCardNo(str1))

    # Test Case 2
    str2 = "4155279860457201"
    print(isValidVisaCardNo(str2))

    # Test Case 3
    str3 = "4155279"
    print(isValidVisaCardNo(str3))

    # Test Case 4
    str4 = "6155279860457"
    print(isValidVisaCardNo(str4))

    # Test Case 5
    str5 = "415a27##60457"
    print(isValidVisaCardNo(str5))