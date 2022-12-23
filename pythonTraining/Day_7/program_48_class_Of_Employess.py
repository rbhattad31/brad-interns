class Employee:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)


emp = Employee("Sam", 36)
emp.details()
