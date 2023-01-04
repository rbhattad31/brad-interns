class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary

    def details(self):
        print(self.name,self.age,self.__salary)

class sub(Employee):
    def employee(self,name,age,salary):
        print(self.name,self.age,self.salary)

x=sub("Ayush",21,10000)
print(x.age)
