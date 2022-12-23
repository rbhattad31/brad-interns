d1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four'}
d2 = {'a': 1, 'b': 2, 3: 'Three', (1, 2): 34}
print(d1[1])
print(d2['b'])
print(d2.get(1, 2))
# How to get all the keys in dictionary
dic = {1: 'One', 2: 'two', 3: 'three', 4: 'Four', 5: 'Five', 6: 'Six', 7:  'Seven'}
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))
dic[8] = "eight"
dic[0] = "zero"
print(dic)
# common operators
print(1 in dic)
print(100 in dic)
print(dic == dic.copy())
# removing values from dictionary
print(dic.pop(0))
print(dic)
print(dic.popitem())
print(dic)
del dic[5]
print(dic)
