testcase = input()
print('UnicodeEncodeError:')
print(ord(testcase[-1]))

b: bytes = testcase.encode('utf8')
print(b)
# doing decoding
print('UnicodeDecodeError:')
print(b.decode('utf8'))
