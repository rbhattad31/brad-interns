import numpy as np
arr = np.array([[2, 8, 9, 4],
                   [9, 4, 9, 4],
                   [4, 5, 9, 7],
                   [2, 9, 4, 3]])
print("Mean of all elements is" ,np.mean(arr))
print("Mean of all row elements is" ,np.sum(np.mean(arr,axis=1)))
print("Mean of all column elements is" ,np.sum(np.mean(arr,axis=0)))
print("Median is" ,np.median(arr))
print("Standard Deviation is" ,np.std(arr))
