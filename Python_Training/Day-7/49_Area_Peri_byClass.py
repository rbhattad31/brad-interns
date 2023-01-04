class Square:
    def __init__(self,s):
        self.s=s

    def area(self):
        print("The Area of Square is %d" %(s*s))

    def perimeter(self):
        print("The Perimeter of Square is %d" %(4*s))

s=int(input("Enter the Side"))
Square(s).area()
Square(s).perimeter()
