import datetime
from tabulate import tabulate
from colorama import Fore, Style
from validation_path import path
from transactions import Transaction

class PaymentMangement:
    headers = ["ID", "Name", "Branch", "Age", "Address", "Phone", "Fine", "Status"]
    t_headers = ["Transaction Id", "Amount", "User Id", "Transaction Date", "Payment Type"]
    def pay_fine(self):
        table_data = []
        user_id = input("Enter the user id:-")
        try:
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)
        else:
            for member in mList:
                if user_id == member.split(", ")[0]:
                    memberList = member.split(", ")
                    table_data.append(memberList)
                    print(tabulate(table_data, headers=PaymentMangement.headers, tablefmt="fancy_grid"))
                    
                    amount = float(input("Enter the Amount:-"))
                    date = str(datetime.date.today())
                    ptype = input("Enter payment type:-")

                    t1 = Transaction(amount, user_id, date, ptype)

                    memberList[6] = float(memberList[6]) - amount
                    if memberList[6] == 0:
                        memberList[7] = "active"
                    updateMember = f'{memberList[0]}, {memberList[1]}, {memberList[2]}, {memberList[3]}, {memberList[4]}, {memberList[5]}, {memberList[6]}, {memberList[7]}'
                    data = mData.replace(member, updateMember)

                    with open(path + "member.txt", "w") as fp:
                        fp.write(data)
                        
                    with open(path + "transactions.txt", 'a') as fp:
                        fp.write(str(t1)+"\n")
                        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully Pay Fine Transaction..." + Style.RESET_ALL)
                        break
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)
                
                return
            
    def show_all_transaction(self):
        table_data = []
        try:
            with open(path + "transactions.txt", "r") as fp:
                allData = fp.read()

        except FileNotFoundError as e:
            print("error:",e)

        else:
            tdata = allData.split("\n")
            for value in tdata:
                if value != "":
                    row = value.split(', ')
                    table_data.append(row)

            print(tabulate(table_data, headers=PaymentMangement.t_headers, tablefmt="fancy_grid"))


        
