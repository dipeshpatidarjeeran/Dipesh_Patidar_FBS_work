# 4. Create a class College which has collection of students. Add the
# following methods :
    # a. Parameteried constructor for number of students.
    # b. AddStudent
    # c. GetStudent
    # d. RemoveStudent
    # e. Override __str__ Method
dict1 ={}
class College:
    def __init__(self, roll_no, name, course):
        self.r_n = roll_no
        self.name = name
        self.course = course

    def addStudent(self):
        dict1[self.r_n] = f'{self.r_n}, {self.name}, {self.course}'
    
    def getStudent(self):
        if self.r_n in dict1:
            return dict1[self.r_n]
        else:
            return 'student not present'

    def removeStudent(self):
        if self.r_n in dict1:
            dict1.pop(self.r_n)

    def __str__(self):
        pass

c1 = College(1,'dipesh','python')
c2 = College(2,'ram','java')
c3 = College(3,'jay','C')

c1.addStudent()
c2.addStudent()
c3.addStudent()

print("Get student:",c2.getStudent())
print(dict1)
c1.removeStudent()
print(dict1)