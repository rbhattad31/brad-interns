# palindrome
user_input = input("Enter the input: ")
reverse = user_input[::-1]  # stepbackward by 1
if user_input == reverse:
    print("Yes it is palindrome")
else:
    print("No it is Not palindrome")
