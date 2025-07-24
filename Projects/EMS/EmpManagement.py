from tabulate import tabulate
from employee import Employee

class EmployeeManagement:
    headers = ["ID", "Name", "Age", "Dept", "Salary"]

    def addEmployee(self):
        Id = input("Enter the Employee ID:-")
        name = input("Enter the Employee name:-")
        age = int(input("Enter the Age:-"))
        dept = input("Enter the department:-")
        sal = float(input("Enter the salary:-"))

        e1 = Employee(Id, name, age, dept, sal)

        with open("Projects/EMS/Employee.txt", "a") as fp:
            fp.write(str(e1)+"\n")
            print("Successfully Add Employee...")


    def GetEmployee(self):
        table_data =[]
        Id = input("Enter the Employee Id:-")

        try:
            with open("Projects/EMS/Employee.txt", "r") as fp:
                empData = fp.read()
                empList = empData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)

        else:
            for emp in empList:
                if Id in emp:
                    row = emp.split(", ")
                    table_data.append(row)
                    print(tabulate(table_data, headers=EmployeeManagement.headers, tablefmt="pretty"))
                    break
            else:
                print("Employee not found.")


    def updateEmployee(self):
        Id = input("Enter the Employee Id:-")
        try:
            with open("Projects/EMS/Employee.txt", "r") as fp:
                empData = fp.read()
                empList = empData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)
        else:
            for emp in empList:
                if Id in emp:
                    elist = emp.split(", ")

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

                    updateEmp = f'{elist[0]}, {elist[1]}, {elist[2]}, {elist[3]}, {elist[4]}'
                    data = empData.replace(emp, updateEmp)

                    with open("Projects/EMS/Employee.txt", "w") as fp:
                        fp.write(data)
                        print("Successfully Update Employee")
                        break
            else:
                print("Employee not found.")


    def deleteEmployee(self):
        Id = input("Enter the Employee Id:-")
        try:
            with open("Projects/EMS/Employee.txt", "r") as fp:
                allData = fp.read()
                empData = allData.split("\n")

        except FileNotFoundError as e:
            print("error:",e)
        else:
            for emp in empData:
                if Id in emp:
                    data = allData.replace(emp, "")
                    with open("Projects/EMS/Employee.txt", "w") as fp:
                        fp.write(data)
                    print("Successfully Delete Employee Details")
                    break
            else:
                print("Employee not found.")


    def showAllEmployee(self):
        table_data = []
        try:
            with open("Projects/EMS/Employee.txt", "r") as fp:
                allData = fp.read()

        except FileNotFoundError as e:
            print("error:",e)

        else:
            empdata = allData.split("\n")
            for value in empdata:
                if value != "":
                    row = value.split(', ')
                    table_data.append(row)

            print(tabulate(table_data, headers=EmployeeManagement.headers, tablefmt="pretty"))
