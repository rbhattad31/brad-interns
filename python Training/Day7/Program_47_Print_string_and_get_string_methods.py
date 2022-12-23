class MyClass:
    def __init__(self):
        self.name = None

    def get_string(self):
        self.name = input("What is your name? :")

    def print_string(self):
        print(self.name.upper())


my_object = MyClass()
my_object.get_string()
my_object.print_string()