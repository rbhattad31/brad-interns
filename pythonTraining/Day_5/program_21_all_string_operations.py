# using_single_quotes_&_double_quotes
string_1 = 'Python programming'
string_2 = "Python programming"
print(string_1)
print(string_2)
print()

# string_type_variables
name = 'python'
print(name)
message = 'Hello world'
print(message)
print()

# Access_string_characters
greet = 'Hello'
print(greet[2])  # "l"
print()

# negative_indexing
greeting = 'hello,hey'
print(greeting[-4])  # ","
print()

# slicing
wish = 'Hii'
wishing_1 = 'wishing'
print(wish[1:2])
print(wishing_1[0:4])
print()

# strings_r_immutable
# message = 'hola amigos'
# message[0] = 'H'
# print()

# we_can_assign_the_variableName_to_A_newString
message_2 = 'Hola Amigos'
message_3 = 'Hello World'
print(message_2)
print(message_3)
print()

# Multiline_string
message_3 = """ 
Never gonna give you up
Never gonna let you down
"""
print(message_3)
print()

# Python_string_operations

# compare_two_strings

str_1 = 'Hello'
str_2 = 'hello'
str_3 = 'hi'
print(str_1 == str_2)
print(str_2 == str_3)
print()

# join_strings
greet_1 = "Hello, "
name_1 = "Jack"

result = greet_1 + name_1
print(result)
print()

# iterate_through_a_python_string '

greet_3 = 'Hello'
for i in greet_3:
    print(i)
print()

# len_of_str
print(len(greet_3))
print()

# string_membership_test
print('a' in 'program')
print('ar' in 'battle')
print()

# upper_case
mssg = 'python is fun'
print(mssg.upper())
# lower_case
msg = 'PYTHON IS FUN'
print(msg.lower())
print()

# string_partition & replace
sttr = 'Python is fun'
print(sttr.partition('is '))
print(type(sttr.partition('is ')))
text = 'bat ball'
replaced_text = text.replace('b','c')
print(replaced_text)
print()

# casefold
text = "pYthon"
lowercased_string = text.casefold()
print(lowercased_string)
print()

# string_center & count
sen = "Python is aawesome"
new_string = sen.center(24,'*')
print(new_string)
print(new_string.count('a'))
print()

# python_endswith
message = 'Python is fun'
print(message.endswith('fun'))
print()

# isdigit
str_11 = '342'
str_22 = 'Python'
print(str_11.isdigit())
print(str_22.isdigit())
print()

# isdecimal
s = "28212"
s_2 ="32ladk3"
print(s.isdecimal())
print(s_2.isdecimal())
print()

# istrip,split,startswith
random = '  this is good '
print(random.lstrip())
print(random.lstrip('sti'))

text_12 = 'Python is a fun programming language'
print(text_12.split(' '))
print(text_12.startswith('Python'))
print()





