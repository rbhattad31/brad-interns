import re  # import getpass
pattern = re.compile(r'')
while True:
    password = input('enter the password :')   # getpass.getpass
    if len(password) < 6:
        print('password must be 6 characters long')
    elif re. search(r'[!@#$%&]', password) is None:
        print('password must contain one special symbol')
    elif re.search(r'\d', password) is None:
        print('password must contain one digit')
    elif re.search('[A-Z],password') is None:
        print("password must contain one capital letter")
    elif re.match(r'[a-z A-Z 0-9 !@#$%&]{6}', password):
        pattern = re.compiler(r'[a-z A-Z 0-9 !@#$%&]{6}', password)
        result = pattern.match(password)
        print('password is correct')
        break
    else:
        print('password invalid')
