import numpy as np
arr = np.array([[2, 8, 9, 4],
                   [9, 4, 9, 4],
                   [4, 5, 9, 7],
                   [2, 9, 4, 3]])
print("The sum of all columns wise is" ,np.sum(arr,axis=0))
