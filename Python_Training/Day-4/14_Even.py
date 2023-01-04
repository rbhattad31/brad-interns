a=[]
n=int(input("Enter the no of elements"))

for i in range(0,n):
    element=int(input())
    a.append(element)

b=[x for x in a if(x%2==0)]
print(b)
