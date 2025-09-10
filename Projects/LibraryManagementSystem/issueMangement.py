import datetime
from tabulate import tabulate
from colorama import Fore, Style
from issuebook import IssueBook
from validation_path import path, get_input, create_logs


class IssueMangement:
    
    headers = ["Member_Id", "Book_Id", "Issue_Date", "Return_Date"]

    def issue_book(self):
        mid = get_input("Enter the Member Id:-")
        bid = get_input("Enter the Book Id:-")

        try:
            with open(path + "bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")
            with open(path + "issueBook.txt", "r") as fp:
                iData = fp.read()
                isulist = iData.split("\n")

        except FileNotFoundError as e:
            print("error:", e)
            return

        for member in mList:
            if mid == member.split(", ")[0]:
                break
        else:
            print(Style.BRIGHT + Fore.RED + "⚠️  Member not found." + Style.RESET_ALL)
            return

        for book in bList:
            boollist = book.split(", ")
            if bid == boollist[0] and boollist[6] == "available":
                member_id = mid
                book_id = bid
                issue_date = str(datetime.date.today())
                return_date = str(datetime.date.today() + datetime.timedelta(days=5))

                # check already issued
                for isbook in isulist:
                    if not isbook.strip():
                        continue
                    issueb = isbook.split(", ")
                    if member_id == issueb[0] and book_id == issueb[1]:
                        print("⚠️ Book already issued")
                        return

                # ✅ Step 3: prepare updated data (in memory only)
                new_issue_line = str(IssueBook(member_id, book_id, issue_date, return_date))

                boollist[5] = str(int(boollist[5]) + 1)

                if int(boollist[5]) == int(boollist[4]):
                    boollist[6] = "not available"

                updatebook = f'{boollist[0]}, {boollist[1]}, {boollist[2]}, {boollist[3]}, {boollist[4]}, {boollist[5]}, {boollist[6]}'
                new_bData = bData.replace(book, updatebook)
                new_iData = iData + ("\n" if iData.strip() else "") + new_issue_line

                # ✅ Step 4: only write if everything is successful
                try:
                    with open(path + "bookDetails.txt", "w") as fp:
                        fp.write(new_bData)

                    with open(path + "issueBook.txt", "w") as fp:
                        fp.write(new_iData)

                    print(
                        Style.BRIGHT + Fore.GREEN +
                        f"✅ Book '{book_id}' issued successfully to member '{member_id}' on {issue_date} "
                        f"and return date is {return_date}." + Style.RESET_ALL
                    )
                    create_logs("Book Issued", f"Book {bid} issued to Member {mid}")
                except Exception as e:
                    print("⚠️ Error while saving data:", e)
                break
        else:
            print(Style.BRIGHT + Fore.RED + "⚠️  Book not found or Not Available...." + Style.RESET_ALL)

    def return_book(self):
        mid = get_input("Enter the Member Id:- ")
        bid = get_input("Enter the Book Id:- ")

        try:
            with open(path + "bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")
            with open(path + "member.txt", "r") as fp:
                mData = fp.read()
                mList = mData.split("\n")
            with open(path + "issueBook.txt", "r") as fp:
                iData = fp.read()
                isulist = iData.split("\n")

        except FileNotFoundError as e:
            print("error:", e)
            return

        # ✅ Step 1: check issued book
        for issue in isulist:
            if not issue.strip():
                continue
            iList = issue.split(", ")

            if iList[0] == mid and iList[1] == bid:
                return_date = datetime.datetime.strptime(iList[3], '%Y-%m-%d').date()
                today_date = datetime.date.today()
                days = (today_date - return_date).days
                fine = days * 10 if days > 0 else 0

                new_mData = mData
                new_bData = bData
                new_iData = iData

                # ✅ Step 2: update member (fine handling)
                if fine > 0:
                    for member in mList:
                        if mid == member.split(", ")[0]:
                            memberList = member.split(", ")
                            memberList[6] = str(int(memberList[6]) + fine)
                            memberList[7] = "pending fine"
                            updateM = f'{memberList[0]}, {memberList[1]}, {memberList[2]}, {memberList[3]}, {memberList[4]}, {memberList[5]}, {memberList[6]}, {memberList[7]}'
                            new_mData = mData.replace(member, updateM)
                            break

                # ✅ Step 3: update book details
                for book in bList:
                    booklist = book.split(", ")
                    if booklist[0] == bid:
                        booklist[5] = str(int(booklist[5]) - 1)
                        booklist[6] = "available"
                        updateb = f'{booklist[0]}, {booklist[1]}, {booklist[2]}, {booklist[3]}, {booklist[4]}, {booklist[5]}, {booklist[6]}'
                        new_bData = bData.replace(book, updateb)
                        break

                # ✅ Step 4: remove from issue list
                new_iData = "\n".join(
                    [line for line in iData.strip().split("\n") 
                    if line.strip() != "" and not (line.split(", ")[0] == mid and line.split(", ")[1] == bid)]
                )


                # ✅ Step 5: write only after everything ready
                try:
                    with open(path + "member.txt", "w") as fp:
                        fp.write(new_mData)

                    with open(path + "bookDetails.txt", "w") as fp:
                        fp.write(new_bData)

                    with open(path + "issueBook.txt", "w") as fp:
                        if new_iData:
                            fp.write(new_iData + "\n")
                        else:
                            fp.write("") 

                    print(
                        Style.BRIGHT + Fore.GREEN +
                        f"✅ Book returned successfully. Fine charged: ₹{fine}." +
                        Style.RESET_ALL
                    )
                    create_logs("Book Returned", f"Book {bid} returned to Member {mid}")
                except Exception as e:
                    print("⚠️ Error while saving data:", e)

                break
        else:
            print(Style.BRIGHT + Fore.RED + "❌ Invalid Book Id or Member Id " + Style.RESET_ALL)

    def show_issued_book(self):
        table_data = []
        try:
            with open(path + "issueBook.txt", "r") as fp:
                allData = fp.read()

        except FileNotFoundError as e:
            print("error:",e)

        else:
            mdata = allData.split("\n")
            for value in mdata:
                if value != "":
                    row = value.split(', ')
                    table_data.append(row)

            print(tabulate(table_data, headers=IssueMangement.headers, tablefmt="fancy_grid"))
