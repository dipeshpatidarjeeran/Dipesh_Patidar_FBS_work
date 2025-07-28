from tabulate import tabulate
from member import Member
from validation_path import path, valid_member_id


class MemberManagement:
    headers = ["ID", "Name", "Branch", "Phone", "Fine"]

    def addMember(self):
        Id = input("Enter the Member ID:-")
        new_id = valid_member_id(Id)
        name = input("Enter the Member Name:-")
        branch = input("Enter the Branch:-")
        phone = int(input("Enter the Phone Number:-"))
        fine = 0
        m1 = Member(new_id, name, branch, phone, fine)

        with open(path + "member.txt", 'a') as fp:
            fp.write(str(m1)+"\n")
            print("Successfully Add Member...")


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
                    print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="pretty"))
                    break
            else:
                print("Member not found.")


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

                    ch = input("Do you want to update title(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[1] = input("Enter the new Title:-")
                    
                    ch = input("Do you want to update author(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[2] = input("Enter the new author:-")
                    
                    ch = input("Do you want to update copies(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[3] = input("Enter the new copies:-")
                    
                    ch = input("Do you want to update status(y/n):-")
                    if ch.lower() in ['y','yes']:
                        memberList[4] = input("Enter the new status:-")

                    updateMember = f'{memberList[0]}, {memberList[1]}, {memberList[2]}, {memberList[3]}, {memberList[4]}'
                    data = mData.replace(member, updateMember)

                    with open(path + "member.txt", "w") as fp:
                        fp.write(data)
                        print("Successfully Update Member")
                        break
            else:
                print("Member not found.")


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
                print("Successfully Delete Member Details")
            else:
                print("Member not found.")


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

            print(tabulate(table_data, headers=MemberManagement.headers, tablefmt="pretty"))
