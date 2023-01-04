a=[]
n=int(input("enter no of elements"))
for i in range(0,n):
    element=int(input())
    a.append(element)
print(a)
x=[]
count=0
for y in a:
    if y not in x:
        count+=1
        x.append(y)

print(count)