# memory error
def fact(a):
    factors = []
    for i in range(1, a + 1):
        if a % i == 0:
            factors.append(i)
    return factors


num = 600851475143
print(fact(num))


#
def func():
    print(ans)


func()


# NotImplementedError
class BaseClass(object):
    """Defines the interface"""

    def __init__(self):
        super(BaseClass, self).__init__()

    def do_something(self):
        """The interface, not implemented"""
        raise NotImplementedError(self.__class__.__name__ + '.do_something')


class SubClass(BaseClass):
    """Implements the interface"""

    def do_something(self):
        """really does something"""
        print(self.__class__.__name__ + ' doing something!')


SubClass().do_something()
BaseClass().do_something()


# OSError
def func(ans=None):
    print(ans)


func()
