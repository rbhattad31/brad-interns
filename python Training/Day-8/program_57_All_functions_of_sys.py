import sys
print(sys.version)
print("******************************************")
# Input and Output using sys
# stdin
# stdout
# std
## stdin ##
import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")
print("*************************************************")
# stdout
import sys

sys.stdout.write('venkat')
