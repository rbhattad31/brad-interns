listA = ['xy-xy', 'pq-qr', 'xp-xp-xp', 'dd-ee']
print("Given list : ", listA)
res = [set(sub.split('-')) for sub in listA]
print("List after duplicate removal : ", res)
