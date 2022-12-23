class Staff:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary:", self.salary)

# inherit from the Staff class
class Employee(Staff):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        super().__init__("Raj", 25, 25000)
employee = Employee("Raj", 25, 25000)

# display all the namespaces
print(employee.__dict__)