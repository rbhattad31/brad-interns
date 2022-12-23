import random

print(random.choice([1, 2, 3, 5, 9]))
print(random.choice('A String'))
print()

# Python Number randrange() Method
print(random.randrange(100, 1000, 2))
print(random.randrange(100, 1000, 3))
print()

# seed
print(random.random())
random.seed(10)
print(random.random())

# It will generate same random number
random.seed(10)
print(random.random())

# It will generate same random number
random.seed(10)
print(random.random())
print()

# shuffle()
list_r = [20, 16, 10, 5]
random.shuffle(list_r)
print(list_r)
random.shuffle(list_r)
print(list_r)
print()

# uniform()
print(random.uniform(5, 10))
print(random.uniform(7, 14))
