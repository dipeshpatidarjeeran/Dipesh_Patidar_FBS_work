from tabulate import tabulate
from employee import Employee

class EmployeeManagement:
    allEmp = {}
    headers = ["ID", "Name", "Age", "Dept", "Salary"]
    def addEmployee(self):
        Id = input("Enter the Employee ID:-")
        name = input("Enter the Employee name:-")
        age = int(input("Enter the Age:-"))
        dept = input("Enter the department:-")
        sal = float(input("Enter the salary:-"))

        e1 = Employee(Id, name, age, dept, sal)
        EmployeeManagement.allEmp[Id] = str(e1)
        print("Successfully Add Employee...")

    def GetEmployee(self):
        table_data =[]
        Id = input("Enter the Employee Id:-")

        if Id in EmployeeManagement.allEmp:
            estr = EmployeeManagement.allEmp[Id]
            row = estr.split(', ')
            table_data.append(row)
            
            print(tabulate(table_data, headers=EmployeeManagement.headers, tablefmt="pretty"))
        else:
            print("Employee not found.")

    def updateEmployee(self):
        Id = input("Enter the Employee Id:-")

        if Id in EmployeeManagement.allEmp:
            estr = EmployeeManagement.allEmp[Id]
            elist = estr.split(", ")

            ch = input("Do you want to update name(y/n):-")
            if ch.lower() in ['y','yes']:
                elist[1] = input("Enter the new name:-")
            
            ch = input("Do you want to update age(y/n):-")
            if ch.lower() in ['y','yes']:
                elist[2] = input("Enter the new age:-")
            
            ch = input("Do you want to update dept(y/n):-")
            if ch.lower() in ['y','yes']:
                elist[3] = input("Enter the new dept:-")
            
            ch = input("Do you want to update salary(y/n):-")
            if ch.lower() in ['y','yes']:
                elist[4] = input("Enter the new salary:-")

            EmployeeManagement.allEmp[Id] = f'{elist[0]}, {elist[1]}, {elist[2]}, {elist[3]}, {elist[4]}'
            print("Successfully Update Employee")
        else:
            print("Employee not found.")

    def deleteEmployee(self):
        Id = input("Enter the Employee Id:-")

        if Id in EmployeeManagement.allEmp:
            EmployeeManagement.allEmp.pop(Id)
            print("Successfully Delete Employee Details")
        else:
            print("Employee not found.")

    def showAllEmployee(self):
        table_data = []
        for value in EmployeeManagement.allEmp.values():
            row = value.split(', ')
            table_data.append(row)

        print(tabulate(table_data, headers=EmployeeManagement.headers, tablefmt="pretty"))