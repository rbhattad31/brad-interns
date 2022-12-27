# Type error
arr = ('tuple',) + 'string'
print(arr)


# UnboundLocalError
def global_name_error(unknown_global_name=None):
    print(unknown_global_name)


def unbound_local(local_val=None):
    local_val = local_val + 1
    print(local_val)


try:
    global_name_error()
except NameError as err:
    print('Global name error:', err)

try:
    unbound_local()
except UnboundLocalError as err:
    print('Local name error:', err)

#