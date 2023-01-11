f=open("Demo.txt","a")
x=input("Write the string to be added")
f.write(x)
f.close()

f=open("Demo.txt","r")
print(f.read())
