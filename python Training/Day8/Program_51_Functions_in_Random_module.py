import random

print("=" * 20)
l11 = [1, 2, 4, 5, 7, 'banana', 8, 9]
print(random.choice(l11))
print("=" * 20)
r1 = random.randint(5, 15)
print("random number between 5 and 15 is {}".format(r1))
print("="*20)
print(random.seed(5))
print(random.random())
print("="*20)
l1 = [1, 3, 4, 6, 'apple', 'mango']
random.shuffle(l1)
print(l1)
print("="*20)
