str_1 = input("Enter a string: ")
str_1 = str_1.lower()
vowels = "aeiou"
dict_of_vowels = dict()
print(dict_of_vowels)
dict_of_vowels = dict_of_vowels.fromkeys(vowels, 0)  #giving with count zero
print(dict_of_vowels)
for char in str_1:
    if char in vowels:
        dict_of_vowels[char] += 1
print(dict_of_vowels)
