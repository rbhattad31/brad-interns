import random
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print("----------------------------------------------------------")
import random
random.seed(10)
print(random.random())  # the generator creates a random number based on the seed value,
print("----------------------------------------------------------")
import random
x = random.getstate()   #
print(x)
print("----------------------------------------------------------")
import random
print(random.getrandbits(8))
print("----------------------------------------------------------")
import random
print(random.randrange(3, 9))
print("----------------------------------------------------------")
import random
print(random.randint(3, 8))
print("----------------------------------------------------------")
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
print("----------------------------------------------------------")
import random
print(random.uniform(20, 60))
print("----------------------------------------------------------")
import random
print(random.triangular(20, 60, 30))
print("----------------------------------------------------------")
