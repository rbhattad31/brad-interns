import string
import random

lower_len = int(input("Enter No of lowercase characters: "))
upper_len = int(input("Enter No of uppercase characters: "))
digit_len = int(input("Enter No of digits characters: "))
symbol_len = int(input("Enter No of  Symboles: "))

pwd_len = lower_len + upper_len + digit_len + symbol_len

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation

strr = random.choices(lower, k=lower_len) + random.choices(upper, k=upper_len) + random.choices(digit, k=digit_len) + random.choices(symbol, k=symbol_len)
print(strr)
random.shuffle(strr)
print(strr)