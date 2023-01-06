class sol2:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def multi(self):
        print("The Product of two numbers is %d " %(x*y))

    def div(self):
        print("The Division of two numbers is %.2f" %(x/y))

x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
sol2(x,y).multi()
sol2(x,y).div()
