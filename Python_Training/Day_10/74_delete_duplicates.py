import re
a=input("Enter text")
x=re.split("\s",a)
list=[]
for y in x:
    if y not in list:
        list.append(y)
for c in list:
    print(c,end=" ")