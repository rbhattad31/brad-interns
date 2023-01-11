f=open("Merge.txt","r")
x=f.readline()
y=f.readlines()
print("No of Characters is" ,len(x))
count=0
for i in range(0,len(x)):
    if(x[i]==" "):
        count=count+1
print("No of blanks in file is" ,count)
z=x.split()
print("No of words in file is" ,len(z))
b=f.readlines()
f.close()

f=open("Merge.txt","r")
c=f.readlines()
print("No of lines is",len(c))





