
class Student:
    def __init__(self, studentId, name, age):
        self.std_id = studentId
        self.name = name
        self.age = age
    
    def Display(self):
        print("Student ID:",self.std_id)
        print("Name:",self.name)
        print("Age:",self.age)

    def Accept(self):
        self.std_id = input("enter the studnet Id:-")
        self.name = input("enter the student name:-")
        self.age = int(input("enter the age:-"))

    def CalculateRank(self):
        if self.inte_marks >= 90:
            print('Rank : A+')
        elif self.inte_marks >= 75:
            print('Rank : A')
        elif self.inte_marks >= 60:
            print('Rank : B')
        elif self.inte_marks >= 40:
            print('Rank : c')
        else:
            print("Fail")
