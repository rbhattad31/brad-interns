class sol1:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        print("The sum of two numbers is %d" %(a+b))

    def subt(self):
        print("The diff of two numbers is %d" %(a-b))


a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
sol1(a,b).sum()
sol1(a,b).subt()


