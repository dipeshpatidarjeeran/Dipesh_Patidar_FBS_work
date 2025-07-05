 ### Static variable:
#1. class level variable
#2. one copy is created
#3. accessed using class name 

### Non-static variable:
#1. object level variable
#2. copies will be depends on how many objects are created
#3. Accessed using object name

class Account:
    bank_name = "SBI"

    def __init__(self,holder_name,ac_no,balance):
        self.hol_nm = holder_name
        self.a_n = ac_no
        self.bal = balance

    def showData(self):
        print("Bank Name:",Account.bank_name)
        print("Holder Name:",self.hol_nm)
        print("Account no:",self.a_n)
        print("balance:",self.bal)
        print("_"*25)

ac1 = Account("deep",10001,12000)
ac1.showData()

ac2 = Account("ram",10002,15000)
ac2.showData()