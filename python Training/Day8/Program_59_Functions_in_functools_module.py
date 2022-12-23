from functools import partialmethod


class Demo:
    def __init__(self):
        self.color = 'black'

    def _color(self, type):
        self.color = type

    set_red = partialmethod(_color, type='red')
    set_blue = partialmethod(_color, type='blue')
    set_green = partialmethod(_color, type='green')


obj = Demo()
print(obj.color)
obj.set_blue()
print(obj.color)