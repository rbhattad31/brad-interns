# overflow error
import sys

print('Regular integer: (maxint=%s)' % sys.maxint)
try:
    i = sys.maxint * 3
    print('No overflow for ', type(i), 'i =', i)
except OverflowError as err:
    print('Overflowed at ', i, err)

print()
print('Long integer:')
for i in range(0, 100, 10):
    print('%2d' % i, 2 ** i)

print()
print('Floating point values:')
try:
    f = 2.0 ** i
    for i in range(100):
        print(i, f)
        f = f ** 2
except OverflowError as err:
    print('Overflowed after ', f, err)
# StopIteration
Arr = [3, 1, 2]
i = iter(Arr)

print(i)
print(i.next())
print(i.next())
print(i.next())
print(i.next())
