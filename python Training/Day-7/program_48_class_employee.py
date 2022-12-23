class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary: ", self.__salary)


EMP = Employee("Venkat", 21, 8000)
EMP.show_details()
