ip_str = input("Enter a string: ")
ip_str = ip_str.casefold()
count = {x: sum([1 for char in ip_str if char == x]) for x in 'aeiou'}
print(count)
Output: {'a': 3, 'e': 3, 'i': 2, 'o': 3, 'u': 1}
