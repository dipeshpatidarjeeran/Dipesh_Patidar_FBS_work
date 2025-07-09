# 3. Create a class MedicalStudent inherited from Student with following
#     a:
#         i. Data members :Specialization
#         ii. MarksOfInternship
#     b. Add the following methods :
#         i. Parameterized constructor
#         ii. Display
#         iii. Accept
#         iv. override Method CalculateRank
#         v. Override __str__ Method

from student_data import Student
class MedicalStudent(Student):
    def __init__(self, studentId, name, age, specialization, marksOfInternship):
        super().__init__(studentId, name, age)
        self.spcliz = specialization
        self.inte_marks = marksOfInternship

    def Accept(self):
        super().Accept()
        self.spcliz = input("which field are you specialized:-")
        self.inte_marks = int(input("enter he marks of internship:-"))

    def Display(self):
        super().Display()
        print("Specialization:",self.spcliz)
        print("Marks of Internship:",self.inte_marks)

    def __str__(self):
        return f'Student Id:{self.std_id}\nName:{self.name}\nAge:{self.age}\nSpecialization:{self.spcliz}\nMarks of Internship:{self.inte_marks}'

    def CalculateRank(self):
        if self.inte_marks >= 80:
            print('Rank : A')
        elif self.inte_marks >= 60:
            print('Rank : B')
        elif self.inte_marks >= 40:
            print('Rank : c')
        else:
            print("Rank : Fail")

m1 = MedicalStudent('m21','dipesh',24,"orthopedic",90)
m1.Accept()
print("#"*25)
print(m1)
m1.CalculateRank()