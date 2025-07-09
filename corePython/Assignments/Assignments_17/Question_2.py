# Create a derived class from Student as EnggStudent with :
#     a. Data members as :
#         i. Branch
#         ii. InternalMarks
#     b. Add the following methods :
#         i. Parameterized constructor
#         ii. Display
#         iii. Accept
#         iv. override Method CalculateRank
#         v. Override __str__ Method
from student_data import Student

class EnggStudnet(Student):
    def __init__(self, studentId, name, age, branch, internal_marks):
        super().__init__(studentId, name, age)
        self.branch = branch
        self.inte_marks = internal_marks

    def __str__(self):
        return f'Student Id:{self.std_id}\nName:{self.name}\nAge:{self.age}\nBranch:{self.branch}\nInternal Marks:{self.inte_marks}'
    
    def Accept(self):
        super().Accept()
        self.branch = input("Enter the branch name:-")
        self.inte_marks = int(input("Enter the internal marks:-"))

    def Display(self):
        super().Display()
        print("Branch:",self.branch)
        print("Internal marks:",self.inte_marks)

    def CalculateRank(self):
        if self.inte_marks >= 90:
            print('Rank : A+')
        elif self.inte_marks >= 85:
            print('Rank : A')
        elif self.inte_marks >= 70:
            print('Rank : B+')
        elif self.inte_marks >= 50:
            print('Rank : B')
        elif self.inte_marks >= 40:
            print("Ranl : C")
        else:
            print("Rank : Fail")
    
    

e1 = EnggStudnet('s21','dipesh',24,"CS",90)
e1.Accept()
print("#"*25)
print(e1)
e1.CalculateRank()