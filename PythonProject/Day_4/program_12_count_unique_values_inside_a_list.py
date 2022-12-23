list = ['apple', 'banana', 'cherry', 'apple', 'cherry', 'lemon']
from collections import Counter
counter_object = Counter(list)
keys = counter_object == Counter(list)
keys = counter_object.keys()
num_values = len(keys)
print(num_values)

