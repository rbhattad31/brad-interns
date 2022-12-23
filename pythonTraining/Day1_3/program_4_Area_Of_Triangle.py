# Python Program to find Area of a Triangle using Functions
import math
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a+b+c)/2
Area_of_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(round(Area_of_triangle, 2))
