class Student:
    #Properties/Attributes
    name = ("Ann")
    gender = ("female")

    #Behaviour/Method
    def study(self):
        print("Student is studying")


student1 = Student() #Creating an object
student1.study()
print(student1.name)


student2 = Student()