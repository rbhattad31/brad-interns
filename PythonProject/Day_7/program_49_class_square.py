class square:
    def areaOfSquare(self, s):
        return s*s

print("Enter the Side Length of Square: ", end="")
l = float(input())
obj = square()
a = obj.areaOfSquare(l)

print("\nArea = {:.2f}".format(a))


class perimeterofsqr:
    def findPerSqr(self, x):
        return 4*x

print("Enter the Side Length: ", end="")
s = float(input())
ob = perimeterofsqr()
p = ob.findPerSqr(s)
print("\nPerimeter = {:.2f}".format(p))