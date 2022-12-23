import random
import string
print(string.ascii_letters)
print(string.printable)


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(result_str)


password = ''.join(random.choice(string.printable) for i in range(10))
print("Random password is:", password)
get_random_string(10)