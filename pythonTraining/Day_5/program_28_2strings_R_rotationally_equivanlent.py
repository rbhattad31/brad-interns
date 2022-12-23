test_str1 = 'hellohi'
test_str2 = 'hihello'
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))
print()
res = any(''.join([test_str2[idx2 - idx1]
for idx2, val2 in enumerate(test_str2)]) == test_str1
for idx1, val1 in enumerate(test_str1))
print("Are two strings Rotationally equal ? : " + str(res))
