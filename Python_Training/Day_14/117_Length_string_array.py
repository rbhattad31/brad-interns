import numpy as np
arr = np.array(['bmw','mercedes','audi','porsche','jaguar'])
for i in range(0,len(arr)):
  print("Length of element at index %d is %d" %(i,len(arr[i])))

for j in range(0,len(arr)):
  arr[j]=arr[j].swapcase()

print(arr)
