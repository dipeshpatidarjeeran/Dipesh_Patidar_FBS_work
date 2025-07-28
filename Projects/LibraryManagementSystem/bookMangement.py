from tabulate import tabulate
from book import Book
from validation_path import path, valid_id


class BookManagement:
    headers = ["ID", "title", "author", "copies", "bcount", "status"]

    def addBook(self):
        Id = input("Enter the Book ID:-")
        new_id = valid_id(Id)
        title = input("Enter the Book title:-")
        author = input("Enter the author:-")
        copies = int(input("Enter the Book copies:-"))
        status = "available"
        bcount = 0
        b1 = Book(new_id, title, author, copies, bcount, status)

        with open(path + "bookDetails.txt", 'a') as fp:
            fp.write(str(b1)+"\n")
            print("Successfully Add Book...")


    def GetBook(self):
        table_data =[]
        Id = input("Enter the Book Id:-")

        try:
            with open(path + "bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)

        else:
            for book in bList:
                if Id in book:
                    row = book.split(", ")
                    table_data.append(row)
                    print(tabulate(table_data, headers=BookManagement.headers, tablefmt="pretty"))
                    break
            else:
                print("Book not found.")


    def updateBook(self):
        Id = input("Enter the Book Id:-")
        try:
            with open(path + "bookDetails.txt", "r") as fp:
                bData = fp.read()
                bList = bData.split("\n")

        except FileNotFoundError as e:
            print("Error:",e)
        else:
            for book in bList:
                if Id in book:
                    boollist = book.split(", ")

                    ch = input("Do you want to update title(y/n):-")
                    if ch.lower() in ['y','yes']:
                        boollist[1] = input("Enter the new Title:-")
                    
                    ch = input("Do you want to update author(y/n):-")
                    if ch.lower() in ['y','yes']:
                        boollist[2] = input("Enter the new author:-")
                    
                    ch = input("Do you want to update copies(y/n):-")
                    if ch.lower() in ['y','yes']:
                        boollist[3] = input("Enter the new copies:-")
                    
                    ch = input("Do you want to update status(y/n):-")
                    if ch.lower() in ['y','yes']:
                        boollist[4] = input("Enter the new status:-")

                    updatebook = f'{boollist[0]}, {boollist[1]}, {boollist[2]}, {boollist[3]}, {boollist[4]}'
                    data = bData.replace(book, updatebook)

                    with open(path + "bookDetails.txt", "w") as fp:
                        fp.write(data)
                        print("Successfully Update Book")
                        break
            else:
                print("Book not found.")


    def deleteBook(self):
        Id = input("Enter the book Id:-")
        try:
            with open(path + "bookDetails.txt", "r") as fp:
                allData = fp.read()
                bData = allData.strip().split("\n")

            with open(path + "issueBook.txt", "r") as fp:
                issueData = fp.read()
                iData = issueData.strip().split("\n")

        except FileNotFoundError as e:
            print("error:",e)
        else:
            for issue in iData:
                if Id == issue.split(", ")[1]:
                    print("❌ Book cannot be deleted. It is currently issued to a member")
                    return

            new_bData = [book for book in bData if Id not in book]
            if len(new_bData) != len(bData):
                with open(path + "bookDetails.txt", "w") as fp:
                    fp.write("\n".join(new_bData))
                print("Successfully Delete Book Details")
            else:
                print("Book not found.")


    def showAllBook(self):
        table_data = []
        try:
            with open(path + "bookDetails.txt", "r") as fp:
                allData = fp.read()

        except FileNotFoundError as e:
            print("error:",e)

        else:
            bdata = allData.split("\n")
            for value in bdata:
                if value != "":
                    row = value.split(', ')
                    table_data.append(row)

            print(tabulate(table_data, headers=BookManagement.headers, tablefmt="pretty"))
