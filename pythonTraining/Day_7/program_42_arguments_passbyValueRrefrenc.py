student = {'Archana': 28, 'krishna': 25, 'Ramesh': 32, 'vineeth': 25}


def test(student):
    new = {'alok': 30, 'Nevadan': 28}
    student.update(new)
    return


test(student)
print("outside the function:", student)


# function_in_a_function


def outer_func(name):
    def inner_func(name):
        print(name)
    inner_func(name)


outer_func("hemanth")