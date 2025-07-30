import datetime
from tabulate import tabulate
from colorama import Fore, Style
from member import Member
from transactions import Transaction
from validation_path import path, valid_member_id, get_valid_phone, valid_name


class MemberManagement:
    headers = ["ID", "Name", "Branch", "Age", "Address", "Phone", "Fine", "Status"]

    def addMember(self):
        Id = input("Enter the Member ID:-")
        new_id = valid_member_id(Id)
        name = input("Enter the Member Name:-")
        name = valid_name(name)
        branch = input("Enter the Branch:-")
        age = int(input("Enter the Age:-"))
        address = input("Enter the Address:-")
        new_phone = input("Enter the Phone Number:-")
        phone = get_valid_phone(new_phone)
        fine = 0
        status_input = input("Have you paid  100 rupees the membership fee? (yes/no): ")
        mstatus = "active" if status_input.lower() in ['y','yes'] else "pending"
        if mstatus == "pending":
            fine = 100
        m1 = Member(new_id, name, branch, age, address, phone, fine, mstatus)

        with open(path + "member.txt", 'a') as fp:
            fp.write(str(m1)+"\n")
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully added Member Details!" + Style.RESET_ALL)

        if mstatus == "active":
            amount = 100
            ptype = "membership fee"
            date = str(datetime.date.today())
            t1 = Transaction(amount, new_id, date, ptype)

            with open(path + "transactions.txt", "a") as fp:
                fp.write(str(t1)+"\n")


    def GetMember(self):
        table_data =[]
        Id = input("Enter the Member Id:-")

        try:
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)

        else:
            for member in mList:
                if Id in member:
                    row = member.split(", ")
                    table_data.append(row)
                    print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="fancy_grid"))
                    break
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)



    def updateMember(self):
        Id = input("Enter the member Id:-")
        try:
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)
        else:
            for member in mList:
                if Id in member:
                    memberList = member.split(", ")

                    ch = input("Do you want to update Name(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[1] = input("Enter the new Name:-")
                    
                    ch = input("Do you want to update Branch(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[2] = input("Enter the new Branch:-")
                    
                    ch = input("Do you want to update Age(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[3] = input("Enter the new Age:-")
                    
                    ch = input("Do you want to update Address(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[4] = input("Enter the new Address:-")

                    ch = input("Do you want to update Phone Number(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[5] = input("Enter the new Phone Number:-")

                    ch = input("Do you want to update Membership Status(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[7] = input("Enter the new Status:-")

                    updateMember = f'{memberList[0]}, {memberList[1]}, {memberList[2]}, {memberList[3]}, {memberList[4]}, {memberList[5]}, {memberList[6]}, {memberList[7]}'
                    data = mData.replace(member, updateMember)

                    with open(path + "member.txt", "w") as fp:
                        fp.write(data)
                        print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully Updated Member Details!" + Style.RESET_ALL)
                        break
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)


    def deleteMember(self):
        Id = input("Enter the Member Id:-")
        try:
            with open(path + "member.txt", "r") as fp:
                allData = fp.read()
                mData = allData.strip().split("\n")

            with open(path + "issueBook.txt", "r") as fp:
                issueData = fp.read()
                iData = issueData.strip().split("\n")

        except FileNotFoundError as e:
            print("error:",e)
        else:
            for issue in iData:
                if Id == issue.split(", ")[0]:
                    print("❌ Member cannot be deleted. Book is still issued")
                    return
            
            new_mData = [member for member in mData if Id not in member]
            if len(new_mData) != len(mData):
                with open(path + "member.txt", "w") as fp:
                    fp.write("\n".join(new_mData))
                print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully Deleted Member Details!" + Style.RESET_ALL)
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)


    def showAllMember(self):
        table_data = []
        try:
            with open(path + "member.txt", "r") as fp:
                allData = fp.read()

        except FileNotFoundError as e:
            print("error:",e)

        else:
            mdata = allData.split("\n")
            for value in mdata:
                if value != "":
                    row = value.split(', ')
                    table_data.append(row)

            print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="fancy_grid"))
