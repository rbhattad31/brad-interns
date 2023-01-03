import sys
try:
    s = []
    for i in range(500):
        for j in range(500):
            for k in range(500):
                s.append("more")
    print(s)
except (MemoryError, KeyboardInterrupt) as msg:
    print(msg)

try:
    list1 = [1, 2, 5, 8, 5]
    list2 = [1, 2.0, "hello"]
    print(list1)
    del list1
    print(list1)
except NameError as ne:
    print(ne)


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()