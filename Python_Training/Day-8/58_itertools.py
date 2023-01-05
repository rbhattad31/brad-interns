#infinite iter

import itertools
"""
for i in itertools.count(10, 5):
    if i == 50:
        break
    else:
        print(i, end=" ")
"""
#terminating
"""
import operator
list1 = [2,4,6,8,10,12]
print("The sum is : ", end="")
print(list(itertools.accumulate(list1)))
print("The product is : ", end="")
print(list(itertools.accumulate(list1, operator.mul)))
print("The sum is : ", end="")
print(list(itertools.accumulate(list1)))
print("The product is : ", end="")
print(list(itertools.accumulate(list1, operator.mul)))
"""
#using chain to print all elements
""" 
list1 = [2,4,6,8,10,12]
list2=[1,3,5,7]
list3=[10,11,12,13]
print(list(itertools.chain(list1,list2,list3)))
"""
#dropwhile
"""
list1=[2,4,5,6,8,11,12,14]
print(list(itertools.dropwhile(lambda x:x%2==0,list1)))
"""
#filterfalse(prints which does not satisfy)
"""
list1=[2,4,5,6,8,11,12,14]
print(list(itertools.filterfalse(lambda x:x%2!=0,list1)))
"""
