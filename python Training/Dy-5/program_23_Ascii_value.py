print("please enter the string:", end='')
string = input()
string_length = len(string)
for k in string:
    ASCII = ord(k)
    print(k, "\t", ASCII)
