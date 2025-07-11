from EmpManagement import EmployeeManagement
em = EmployeeManagement()
class Admin:
    def __init__(self):
        ch = 0 
        while(ch != '6'):
            print("""Please select choice
                  1. Add Employee
                  2. Get Employee
                  3. Update Employee
                  4. Delete Employee
                  5. Show All Employee
                  6. logout""")
            
            ch = input("Enter the choice:-")

            if(ch == '1'):
                em.addEmployee()

            elif(ch == '2'):
                em.GetEmployee()

            elif(ch == '3'):
                em.updateEmployee()

            elif(ch == '4'):
                em.deleteEmployee()

            elif(ch == '5'):
                em.showAllEmployee()

            elif(ch == '6'):
                print("logout successful...")

            else:
                print("Invalid choice...Please try again")
