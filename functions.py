#Built In functions - They are also called standard Library Functions
y = max(23,24,54,24,23,23)
print("The maximum value is",y)

x = min(75,57,34,65,84,56,35,68,456,)
print("The minimum value is",x)


# user defined functions
def name():
    print("Darnitto")

name() # Calling a function



def multiply():
    x = 10
    y = 20
    print(x * y)
multiply()


#Parameters/variables and arguments/values
def add(a, b):
    print(a + b)

add(2, 6)


def employee (name, gender, position, salary, age):
    print(name, gender, position, salary, age)

employee("Darnito", "M", "ceo", 200000000, 30)
employee("Joan", "F", "Ass Ceo", 10000000, 20)
employee("Ramah", "M", "Sales Manager", 2005000, 34)
employee("Rappy Keedy", "M", "Marketing Director", 200000, 27)


#a program that displays details of 5 students
def student (fullname, course, age):
    print(fullname, course, age)
student("Dante Darnitto","MIT", "19")
student("Rappy Keedy","Cyber Security", "18")
student("Xander Wize","MIT", "19")
student("Stacy Annest","MIT", "17")
student("Daniel Meent","Data Science", "19")

#Use a user defined function with the parameter and argument
#Full Name, Age, Course, gender