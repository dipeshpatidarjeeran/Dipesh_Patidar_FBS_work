class Person:
    def __init__(self, Id, name, bal):
        self.eid = Id              # public
        self._name = name          # protected
        self.__bal = bal           # private
    
class Employee(Person):
    def __init__(self, Id, name, bal):
        super().__init__(Id, name, bal)

    def display(self):
        print(self.eid)
        print(self._name)
        print(self._Person__bal)

e1 = Employee(101, "Rohit Sharma", 450000)
e1.display()

# print(e1.eid)
# print(e1._name)
# # print(e1.__bal)
# print(e1._Employee__bal)