#### single Level Inheritance
#super class
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.add = address

    def display(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("address:",self.add)

#sub class
class Student(Person):
    def __init__(self, name, age, address, course):
        super().__init__(name, age, address)
        self.course = course

    def display(self):
        super().display()
        print("course:",self.course)

std = Student("dipesh",24,"MP", "python DS")
std.display()