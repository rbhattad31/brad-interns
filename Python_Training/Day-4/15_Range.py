a=[]
n=int(input("Enter no of elements"))
for i in range(0,n):
    element=int(input())
    a.append(element)

x=int(input("Enter the min value of the range"))
y=int(input("Enter the max value of the range"))

for c in a:
    if(c>=x and c<=y):
        print("Elements are in range")
        break

    else:
        print("Elements not in range")
        break
