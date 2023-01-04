a=['Ayush','Ayush Bhattad','Bhattad','BradSol']

a.sort(key=len)
result=[]
for x,y in enumerate(a):
    if y not in ','.join(a[x+1:]):
        result.append(y)

print(result)



