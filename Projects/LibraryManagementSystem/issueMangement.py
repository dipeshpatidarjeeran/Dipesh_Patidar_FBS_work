import datetime
from issuebook import IssueBook

class IssueMangement:
    
    def issue_book(self):
        mid = input("Enter the Member Id:-")
        bid = input("Enter the Book Id:-")

        try:
            with open("Projects/LibraryManagementSystem/data/bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")
            with open("Projects/LibraryManagementSystem/data/issueBook.txt", "r") as fp:
                iData = fp.read()
                isulist = iData.split("\n")

        except FileNotFoundError as e:
            print("error:",e)

        else:
            for member in mList:
                if mid in member.split(", ")[0]:
                    break
            else:
                print("Member not found....")
                return
            
            for book in bList:
                boollist = book.split(", ")
                if bid == boollist[0] and boollist[5] == "available":
                    member_id = mid
                    book_id = bid
                    issue_date = str(datetime.date.today())
                    return_date = "None"

                    for isbook in isulist:
                        issueb = isbook.split(", ")
                        if member_id == issueb[0] and book_id == issueb[1]:
                            print("Book already issued")
                            return
                    else:
                        ib = IssueBook(member_id, book_id, issue_date, return_date)
                        with open("Projects/LibraryManagementSystem/data/issueBook.txt", "a") as fp:
                            fp.write(str(ib)+"\n")

                        boollist[4] = int(boollist[4]) + 1
                        
                        if boollist[4] == int(boollist[3]):
                            boollist[5] = "not available"
                        updatebook = f'{boollist[0]}, {boollist[1]}, {boollist[2]}, {boollist[3]}, {boollist[4]}, {boollist[5]}'
                        data = bData.replace(book, updatebook)
                        with open("Projects/LibraryManagementSystem/data/bookDetails.txt", "w") as fp:
                            fp.write(data)
                            print(f"✅ Book '{book_id}' issued successfully to member '{member_id}' on {issue_date}.")
                            break

            else:
                print("Book not found or Book Not Available....")

    def return_book(self):
        mid = input("Enter the Member Id:- ")
        bid = input("Enter the Book Id:- ")

        try:
            with open("Projects/LibraryManagementSystem/data/bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")
            with open("Projects/LibraryManagementSystem/data/member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")
            with open("Projects/LibraryManagementSystem/data/issueBook.txt", "r") as fp:
                iData = fp.read()
                isulist = iData.split("\n")
                
        except FileNotFoundError as e:
            print("error:",e)
        else:
            for issue in isulist:
                iList = issue.split(", ")
                
                if iList[0] == mid and iList[1] == bid:
                    return_date = datetime.date.today()
                    issue_date = datetime.datetime.strptime(iList[2], '%Y-%m-%d').date()
                    days = (return_date - issue_date).days
                    fine = days * 10 if days > 5 else 0
                    if fine > 0:
                        for member in mList:
                            if mid in member.split(", ")[0]:
                                memberList = member.split(", ")
                                memberList[4] = int(memberList[4]) + fine
                                updateM = f'{memberList[0]}, {memberList[1]}, {memberList[2]}, {memberList[3]}, {memberList[4]}'
                                data = mData.replace(member, updateM)
                                with open("Projects/LibraryManagementSystem/data/member.txt", "w") as fp:
                                    fp.write(data)
                                    break

                    for book in bList:
                        booklist = book.split(", ")
                        # import pdb;pdb.set_trace()
                        if booklist[0] == bid:
                            booklist[4] = int(booklist[4]) - 1
                            booklist[5] = "available"
                            updateb = f'{booklist[0]}, {booklist[1]}, {booklist[2]}, {booklist[3]}, {booklist[4]}, {booklist[5]}'
                            data = bData.replace(book, updateb)
                            with open("Projects/LibraryManagementSystem/data/bookDetails.txt", "w") as fp:
                                fp.write(data)
                                break

                    for issue in isulist:
                        issueList = issue.split(", ")
                        if mid == issueList[0] and bid == issueList[1]:
                            data = iData.replace(issue, "")
                            with open("Projects/LibraryManagementSystem/data/issueBook.txt", "w") as fp:
                                fp.write(data)
                            print(f"✅ Book returned successfully. Fine charged: ₹{fine}")
                            break
                    break
            else:
                print("❌ Book not issued ")
