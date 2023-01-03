import re


def check(s):
	pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if re.match(pattern, s):
		print("Valid Email")
	else:
		print("Invalid Email")

if __name__ == '__main__':

	# Enter the email
	email = input("Enter the Mail id")
	# calling run function
	check(email)
