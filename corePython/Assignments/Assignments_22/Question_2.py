# 2. WAP a menu driven program to perform following operations using
# files :
    # a. Add a record
    # b. Search for a record using id
    # c. Delete a record using id
    # d. Edit a record using id.
    # e. Display all records.
import pickle
from Question_1 import Emp

class EmpManagement:
    def addEmp(self):
        eid = input("enter the emp id:-")
        ename = input("enter the emp name:-")
        dept = input("enter the Dept:-")
        sal = input("enter the salary:-")

        e1 = Emp(eid, ename, dept, sal)
        with open("corePython/Assignments/Assignments_22/emp.txt", "ab") as fp:
            pickle.dump(e1, fp, protocol=pickle.HIGHEST_PROTOCOL)

    def getEmp(self):
        Id = input("enter the emp id:-")
        with open("corePython/Assignments/Assignments_22/emp.txt", "rb") as fp:
            while True:
                try:
                    data = pickle.load(fp)
                    if Id in str(data):
                        print(data)
                except EOFError:
                    break


    def delEmp(self):
        edata = ''
        Id = input("enter the emp id:-")
        with open("corePython/Assignments/Assignments_22/emp.txt", "rb") as fp:
            while True:
                try:
                    data = pickle.load(fp)
                    if Id not in str(data):
                        edata = edata + str(data)
                except EOFError:
                    break

        with open("corePython/Assignments/Assignments_22/emp.txt", "wb") as fp:
            pickle.dump(edata, fp, protocol=pickle.HIGHEST_PROTOCOL)

    def UpdateEmp(self):
        edata = ''
        Id = input("enter the emp id:-")
        with open("corePython/Assignments/Assignments_22/emp.txt", "rb") as fp:
            while True:
                try:
                    data = pickle.load(fp)
                    if Id in str(data):
                        eList = str(data).split(", ")
                        ch = input("Do you want to update Name(y/n):-")
                        if ch.lower() in ['y','yes']:
                            eList[1] = input("Enter the new Name:-")
                        
                        ch = input("Do you want to update Dept(y/n):-")
                        if ch.lower() in ['y','yes']:
                            eList[2] = input("Enter the new Dept:-")
                        
                        ch = input("Do you want to update Salary(y/n):-")
                        if ch.lower() in ['y','yes']:
                            eList[3] = input("Enter the new Salary:-")
                        updateEmp = f"{eList[0]}, {eList[1]}, {eList[2]}, {eList[3]}"
                        edata = edata + updateEmp
                    else:
                        edata = edata + str(data)
                except EOFError:
                    break

        with open("corePython/Assignments/Assignments_22/emp.txt", "wb") as fp:
            pickle.dump(edata, fp, protocol=pickle.HIGHEST_PROTOCOL)

    def showEmp(self):
        with open("corePython/Assignments/Assignments_22/emp.txt", "rb") as fp:
            while True:
                try:
                    data = pickle.load(fp)
                    print(data)
                except EOFError:
                    break

if __name__ == "__main__":
    em = EmpManagement()
    # em.addEmp()
    em.showEmp()
    # em.getEmp()
    # em.delEmp()
    em.UpdateEmp()