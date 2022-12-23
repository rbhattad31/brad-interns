class square:
    def __init__(self,side):
        self.side=side
    def display(self):
        print("side of a square:",self.side)
    def area(self):
        return(self.side*self.side)
    def perimeter(self):
        return(4*self.side)
s=int(input("enter side a square:"))
r1=square(s)
r1.display()
print("Area of square is:",r1.area())
print("Perimeter of a square is:",r1.perimeter())