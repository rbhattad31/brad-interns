import math
a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
#We will use the basic formula for solving any Quadratic Equation
d=b*b-4*a*c
if(d>0):
    sol1=(-b+math.sqrt(d))/(2*a)
    sol2=(-b-math.sqrt(d))/(2*a)
    print("Two Distinct Roots" ,sol1,sol2)
if(d==0):
    sol=(-b)/(2*a)
    print("Equal Solution" ,sol)

if(d<0):
    real=(-b)/(2*a)
    imag=(math.sqrt(-d))/(2*a)
    print("Two complex Roots",complex(real,imag),complex(real,-imag))
