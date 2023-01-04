a=input("Enter a String 1")
b=input("Enter a String 2")
for i in range(len(a)):
    if a[i:]+a[:i]==b:
        print("Equivalent")
        break
