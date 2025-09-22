import datetime, textwrap
from tabulate import tabulate
from colorama import Fore, Style
from member import Member
from logs import Logs
from validation_path import path, valid_member_id, get_valid_phone, valid_name, get_input, create_logs


class MemberManagement:
    headers = ["ID", "Name", "Branch", "Age", "Address", "Phone", "Fine", "Status"]

    def addMember(self):
        Id = get_input("Enter the Member ID:-")
        new_id = valid_member_id(Id)
        name = get_input("Enter the Member Name:-")
        name = valid_name(name)
        branch = get_input("Enter the Profession:-")
        age = int(get_input("Enter the Age:-"))
        address = get_input("Enter the Address:-")
        new_phone = get_input("Enter the Phone Number:-")
        phone = get_valid_phone(new_phone)
        fine = 0
        status_input = get_input("Have you paid  100 rupees the membership fee? (yes/no): ")
        mstatus = "active" if status_input.lower() in ['y','yes'] else "pending fees"
        if mstatus == "pending fees":
            fine = 100
        m1 = Member(new_id, name, branch, age, address, phone, fine, mstatus)

        with open(path + "member.txt", 'a') as fp:
            fp.write(str(m1)+"\n")
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully added Member Details!" + Style.RESET_ALL)
            create_logs("Member Added", f"Member Id {Id} added")

        if mstatus == "active":
            ptype = "membership fee"
            create_logs(ptype, f"100 rupees Membership fee paid by member {Id}")
        else:
            create_logs(mstatus, f"100 rupees Membership fee remains by member {Id}")

    def GetMember(self):
        table_data =[]
        Id = get_input("Enter the Member Id:-")

        try:
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)

        else:
            for member in mList:
                if Id == member.split(", ")[0]:
                    row = member.split(", ")
                    table_data.append(row)
                    print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="fancy_grid"))
                    break
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)



    def updateMember(self):
        Id = get_input("Enter the member Id:-")
        try:
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)
        else:
            for member in mList:
                if Id == member.split(", ")[0]:
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
                        create_logs("Member Updated", f"Member Id {Id} Updated")
                        break
            else:
                print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)


    def deleteMember(self):
        Id = get_input("Enter the Member Id:-")
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
            
            new_mData = [member for member in mData if Id != member.split(", ")[0]]
            if len(new_mData) != len(mData):
                with open(path + "member.txt", "w") as fp:
                    fp.write("\n".join(new_mData) + "\n")
                print(Style.BRIGHT + Fore.LIGHTBLUE_EX + "✅ Successfully Deleted Member Details!" + Style.RESET_ALL)
                create_logs("Member Deleted", f"Member Id {Id} Deleted")
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
                    row[4] = textwrap.fill(row[4],width=15)
                    table_data.append(row)

            print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="fancy_grid"))
