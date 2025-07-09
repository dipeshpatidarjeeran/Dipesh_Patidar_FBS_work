# 1. Create a class Student with following
    # a. data members :
        # i. StudentId
        # ii. Name
        # iii. Age
        # iv. Percentage
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. Method CalculateRank
        # v. Override __str__ Method
class Student:
    def __init__(self, studentId, name, age, percentage):
        self.std_id = studentId
        self.name = name
        self.age = age
        self.per = percentage
    
    def Display(self):
        print("Student ID:",self.std_id)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Percentage:",self.per)

    def __str__(self):
        return f'Student Id:{self.std_id}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.per}'

    def Accept(self):
        self.std_id = input("enter the studnet Id:-")
        self.name = input("enter the student name:-")
        self.age = int(input("enter the age:-"))
        self.per = int(input("enter hte percentage:-"))

    def CalculateRank(self):
        if self.per >= 90:
            print('Rank : A+')
        elif self.per >= 75:
            print('Rank : A')
        elif self.per >= 60:
            print('Rank : B')
        elif self.per >= 40:
            print('Rank : c')
        else:
            print("Fail")
        

s1 = Student('s21','dipesh',24,85)
s1.Accept()
print("#"*25)
print(s1)
s1.CalculateRank()
