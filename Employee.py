from functions import employee


class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def details(self):
        print(self.name,"is the",self.position)

employee1=Employee("DARNITTO","CEO",20000000)
employee2=Employee("Damaris","Managing Director",640000)
employee3=Employee("Joan David","CEO Secretary",1000000)
employee4=Employee("Ian David","Sales Manager",800000)

employee1= Employee("DARNITTO","CEO",20000000)
print(employee1.name,employee1.position,employee1.salary)

employee2= Employee("Damaris","Managing Director",640000)
print(employee2.name,employee1.position,employee1.salary)