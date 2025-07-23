from SY.syMarks import SyMarks
from TY.tyMarks import TyMarks


class Student(SyMarks,TyMarks):
    def __init__(self, roll_no, name, computer, maths, electronics, treory, practical):
        SyMarks.__init__(self, computer, maths, electronics)
        TyMarks.__init__(self, treory, practical)
        self.roll_no = roll_no
        self.name = name
        self.per = 0
        self.total = 0

    def total_marks(self):
        self.total = TyMarks.total_tyMarks(self) + SyMarks.total_syMarks(self)
        self.per = self.total / 5

    def display(self):
        print("Roll Number:",self.roll_no)
        print("Student Name:",self.name)
        print("Total Marks:",self.total)
        print("Percentage:",self.per)

        if self.per >= 70:
            print("Grade: A")
        elif self.per >= 60:
            print("Grade: B")
        elif self.per >= 50:
            print("Grade: C")
        elif self.per >= 40:
            print("Pass Class")
        else:
            print("Fail")


s1 = Student(101,"Dipesh Patidar", 78, 98, 56, 65, 75)
s1.total_marks()
s1.display()