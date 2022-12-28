d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

print('key1' in d)
# True

print('val1' in d)
# False

print('key4' not in d)
# True

# sorting of dict
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)

print(sortedDict)
# ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
