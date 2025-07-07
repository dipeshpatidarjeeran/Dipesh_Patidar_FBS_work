### static method:
#1. class level method
#2. no self parameter
#3. accessed using class name
#4. accessed by obejct with using @staticmethod decorator

### Non-static method:
#1. object level method
#2. self parameter mandatory
#3. accessed using object name

class Student:
    strength = 0
    def __init__(self,name,age,addres):
        self.name = name
        self.age = age
        self.add = addres
        Student.strength += 1

    def showData(self):
        return f"Name:{self.name}\nAge:{self.age}\nAddress:{self.add}"
    @staticmethod
    def totalCount():
        print("total strength:",Student.strength)

obj1 = Student('dipesh',24,"MP")
print(obj1.showData())
print("#"*25)

obj2 = Student('dipesh',24,"MP")
print(obj2.showData())
print("#"*25)

Student.totalCount()
obj2.totalCount()
