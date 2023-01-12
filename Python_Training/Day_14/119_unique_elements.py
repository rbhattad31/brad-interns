import numpy as np
#1-D
arr=np.array([1,2,2,3,4,5,5,5,6])
list=[]
count=0
for x in arr:
  if x not in list:
    count+=1
    list.append(x)
print("No of unique elements is" ,count)
print("Reverse array is ",arr[::-1])
#2-D
arr=np.array([[1,2,2,3],[1,4,4,5],[1,3,3,2],[1,2,3,4]])
list=[]
count=0
for x in np.nditer(arr):
  if x not in list:
    count+=1
    list.append(x)
print("No of unique elements is" ,count)
print("Reverse array is ",arr[::-1])
