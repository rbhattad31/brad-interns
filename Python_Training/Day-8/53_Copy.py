import copy
a = [1, 2, [3,5], 4]
b= copy.copy(a)
print ("The original elements before shallow copying")
for i in range(0,len(a)):
	print (a[i],end=" ")
print("\r")
b[2][0] = 7
print ("The original elements after shallow copying")
for i in range(0,len(a)):
	print (a[i],end=" ")

