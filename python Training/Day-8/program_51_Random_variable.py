# Random variables
import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print("**********************************************************")
# Creating random numbers with seeding value
import random
random.seed(5)
print(random.random())
print(random.random())
print("***********************************************************")
# creating random integers
import random
r1 = random.randint(5, 10)
print("random number between 5 and 10 is %s" % r1)
r2 = random.randint(-10, -1)
print("random number between -10and-1 is %d" % r2)
print("************************************************************")
# Creating Random Floats
from random import random
print(random())
print("************************************************************")
# Selecting Random Elements
import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
string = "venkat"
print(random.choice(string))
tuple1 = (1, 2, 3, 4, 5)
print(random.choice(tuple1))
print("***********************************************************")
# Shuffling List
import random
sample_list=[1,2,3,4,5,6]
print("original list: ")
print(sample_list)
random.shuffle(sample_list)
print("\n after the first shuffle ")
print(sample_list)
random.shuffle(sample_list)
print("\n after the second shuffle ")
print(sample_list)
print("****************************************************")