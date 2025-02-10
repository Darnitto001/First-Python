#Parent/super/Base Class
class Animal:
    def speak(self):
        print('Animal is speaking')

#Child class/Sub class/Derived class
class Dog:
    def bark(self):
        print('Dog is barking')

class Cat:
    def meaouw(self):
        print('Cat is meaouwing')

a = Animal()


d = Dog()
d.speak()


c = Cat()