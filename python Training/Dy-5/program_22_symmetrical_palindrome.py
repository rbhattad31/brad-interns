string=input(("enter the word:"))
print(string)
print(string[::-1])
if(string==string[::-1]):
    print("the word is palindrome")
else:
    print("the word is not palindrome")
