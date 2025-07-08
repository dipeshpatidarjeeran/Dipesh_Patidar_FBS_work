### Multi Level Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Employee(Person):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept

    def display(self):
        super().display()
        print("Dept:",self.dept)

class Hr(Employee):
    def __init__(self, name, age, dept, recru_count):
        super().__init__(name, age, dept)
        self.rec_count = recru_count

    def display(self):
        super().display()
        print("recrutment count:",self.rec_count)

h1 = Hr('dipesh',24, "HR", 4)
h1.display()