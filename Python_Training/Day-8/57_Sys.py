import sys
#for version of system
#print(sys.version)

#for input(stdin)
"""
for line in sys.stdin:
	if 'q' == line.rstrip():
		break
	print(f'Input : {line}')

print("Exit")
"""

#for output(stdout)
#sys.stdout.write('Ayush Bhattad')

#for exception(stderr)
"""
def print_to_stderr(*a):
	print(*a, file = sys.stderr)

print_to_stderr("Ayush Bhattad")
print_to_stderr("BradSol")
"""
#exiting the program
"""
weight= 80
if weight>90:
    sys.exit("Weight is greater than 90")
else:
    print("Weight is less than 90")
"""
