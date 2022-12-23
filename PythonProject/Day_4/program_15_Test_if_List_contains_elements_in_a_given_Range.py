test_list = [4, 5, 6, 11, 7, 3, 9, 20]
print("The original list is : " + str(test_list))
i, j = 1, 10
result = True
for element in test_list:
   print(element)
   if element < i or element >= j:
       result = False
       break
print("Does list contain all elements in range : " + str(result))
