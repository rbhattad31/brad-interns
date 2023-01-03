testcase = input()
print('UnicodeEncodeError:')
print(ord(testcase[-1]))

b: bytes = testcase.encode('utf-8')
print(b)

print('UnicodeDecodeError:')
print(b.decode('utf-8'))
