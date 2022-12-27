# import error
import module_does_not_exist
from exceptions import Userexception
print("******************************************")
# index error

array = [0, 1, 2]
print(array[3])
# key error
array = {'a': 1, 'b': 2}
print(array['c'])
# exception KeyboardInterrupt
try:
    print ('Press Return or Ctrl-C:',)
    ignored = input()
except Exception as err:
    print('Caught exception:', err)
except KeyboardInterrupt as err:
    print('Caught KeyboardInterrupt')
else:
    print ('No exception')

