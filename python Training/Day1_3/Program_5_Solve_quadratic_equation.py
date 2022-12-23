import cmath

print("General form of quadratic equation is : ax**2+bx+c=0")
a = float(input("enter value of a : "))
b = float(input("enter value of b : "))
c = float(input("enter value of c : "))
d = (b ** 2) - (4 * a * c)
if d > 0:
    print("roots are real and different")
elif d == 0:
    print("roots are equal and real")
elif d < 0:
    print("roots are complex")
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print("solutions for quadratic equation are {} and {}".format(sol1, sol2))
