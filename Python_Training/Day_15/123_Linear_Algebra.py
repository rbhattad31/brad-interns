from scipy import linalg
import numpy as np
#solving two equations
a=np.array([[1,2],[5,4]])
b=np.array([10,20])
res=linalg.solve(a,b)
print(res)
#inverse of a matrix
x=np.array([[1,2,2],[4,5,6],[7,8,9]])
inverse=linalg.inv(x)
print(inverse)
pseudo_inv=linalg.pinv(x)
print(pseudo_inv)
#to find determinant
d=linalg.det(a)
print(d)
#single Value Decomposition
x,y,z=linalg.svd(a)
print(x,y,z)
#To find Eigen Values and Eigen Vectors
value,vector=linalg.eig(a)
print(value)
print(vector)
#to find norm
l2=linalg.norm(a)
l1=linalg.norm(a,1)
print(l1)
print(l2)
# various functions on matrix
print(linalg.sqrtm(a))
print(linalg.expm(a))
print(linalg.sinm(a))
print(linalg.cosm(a))