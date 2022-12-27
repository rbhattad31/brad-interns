#syntax error
try:
    print(eval('hello python'))
except SyntaxError as err:
    print('Syntax error %s (%s-%s): %s' % (err.filename, err.lineno, err.offset, err.text))
    print(err)
print("************************************************************")
# indentation
site = 'fb'

if site == 'fb':
    print('Logging on to facebook...')
else:
    print('retype the URL.')
print('All set !')
print("*************************************************************")
# Tab error
if len('hi') == 2:
    print('a')
print('b')
print("*************************************************************")
# system error
try:
    print (eval('geeks for geeks'))
except SyntaxError as err:
    print('Syntax error %s (%s-%s): %s' % (err.filename, err.lineno, err.offset, err.text))
    print (err)
