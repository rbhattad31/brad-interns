f=open('Demo.txt')
#total=f.readlines()
#print("Total lines is" ,len(total))
x=input("Enter a string")
if x in f.read():
    print("It is present in given file")
else:
    print("Not present")