test_dict = {'abc': 11, 'def': 2, 'ghi': 11, 'jkl': 8, 'mno': 2}
print("The original dictionary is :"+str(test_dict))
temp = min(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]
print("keys with minimum values are :"+str(res))
