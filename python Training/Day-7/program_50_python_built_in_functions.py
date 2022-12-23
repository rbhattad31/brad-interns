# 1. abs(x)
a = 12
b = -4
c = 3+4j
d = 7.90
print(abs(a))
print(abs(b))
print(abs(c))
print(abs(d))
print("*****************")
# 2. all(x)
Tuple = (0, True, False)
x = all(Tuple)
print(x)
print("*******************")
# 3.any(x)
my_set = {0, 1, 0}
x = any(my_set)
print(x)
print("******************")
# 4.bin
a = 5
print(bin(a))
print("********************")
# 5.round
print(round(4.5))
print(round(-7.7))
print("***********************")
# 6 bool
print(bool(0))
print(bool(-4.5))
print(bool(None))
print(bool("false"))
print("*******************")
# 7. list
print(list())   # returns empty list
string_obj = 'PALINDROME'
print(list(string_obj))
tuple_obj = ('a', 'e', 'i', 'o', 'u')
print(list(tuple_obj))
list_obj = ['1', '2', '3', 'o', '10u']
print(list(list_obj))
print("**********************")
# 8. len
string_obj = 'PALINDROME'
print(len(string_obj))
tuple_obj = ('a', 'e', 'i', 'o', 'u')
print(len(tuple_obj))
list_obj = ['1', '2', '3', 'o', '10u']
print(len(list_obj))
print("*************************")
# 9.max
num = [11, 22, 45, 84, 76]
print('maximum is:', max(num))
print("***********************")
# 10. power
print(pow(2, -3))
print(pow(2, 4.5))
print(pow(3, 0))
