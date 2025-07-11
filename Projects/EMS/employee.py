class Employee:
    def __init__(self, Id, name, age, dept, sal):
        self.eid = Id
        self.name = name
        self.age = age
        self.dept = dept
        self.sal = sal

    def __str__(self):
        return f'{self.eid}, {self.name}, {self.age}, {self.dept}, {self.sal}'