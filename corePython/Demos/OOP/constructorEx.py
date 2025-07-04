### Constructor:
#1. special method, called automatically when object of that class is created.
#2. user __init__ as the function name
#3. we pass parameters to constructor in the time of object creating.
#4. Type:
    # default / parameterless constructor
    # parameterizes constructor

class Student:
    def __init__(self,roll_no, name, course, address):
        self.rn = roll_no
        self.nm = name
        self.course = course
        self.add = address

    def display(self):
        print("Roll No:",self.rn)
        print("Name:",self.nm)
        print("Course:",self.course)
        print("address:",self.add)
        print("_"*20)

s1 = Student(1,'dipesh','core python','MP')
s1.display()

s2 = Student(2,'ram', 'core java','neemuch')
s2.display()