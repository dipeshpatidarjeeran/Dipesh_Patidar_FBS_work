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
