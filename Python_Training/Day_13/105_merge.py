import os
f=open("Demo.txt","r")
x=f.read()
g=open("Demo2.txt","r")
y=g.read()
z=x+". "+y
file = 'Merge.txt'
with open(os.path.join(file), 'w') as fp:
    pass
h=open("Merge.txt","a")
h.write(z)
h.close()

h=open("Merge.txt","r")
print(h.read())

