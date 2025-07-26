from tabulate import tabulate
from member import Member

class MemberManagement:
    headers = ["ID", "Name", "Branch", "Phone", "Fine"]

    def addMember(self):
        Id = input("Enter the Member ID:-")
        name = input("Enter the Member Name:-")
        branch = input("Enter the Branch:-")
        phone = int(input("Enter the Phone Number:-"))
        fine = 0
        m1 = Member(Id, name, branch, phone, fine)

        with open("Projects/LibraryManagementSystem/data/member.txt", 'a') as fp:
            fp.write(str(m1)+"\n")
            print("Successfully Add Member...")


    def GetMember(self):
        table_data =[]
        Id = input("Enter the Member Id:-")

        try:
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
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
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
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

                    with open("Projects/LibraryManagementSystem/data/member.txt", "w") as fp:
                        fp.write(data)
                        print("Successfully Update Member")
                        break
            else:
                print("Member not found.")


    def deleteMember(self):
        Id = input("Enter the Member Id:-")
        try:
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
                allData = fp.read()
                mData = allData.split("\n")

        except FileNotFoundError as e:
            print("error:",e)
        else:
            for Member in mData:
                if Id in Member:
                    data = allData.replace(Member, "")
                    with open("Projects/LibraryManagementSystem/data/member.txt", "w") as fp:
                        fp.write(data)
                    print("Successfully Delete Member Details")
                    break
            else:
                print("Member not found.")


    def showAllMember(self):
        table_data = []
        try:
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
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
