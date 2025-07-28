path = "C:/Users/HP/Desktop/FBS/Projects/LibraryManagementSystem/data/"


def valid_id(Id):
    with open(path + "bookDetails.txt", "r") as fp:
        bData = fp.read().strip().split("\n")
    for book in bData:
        if book.strip() == "":
            continue
        book_id = book.split(", ")[0]
        if Id == book_id:
            print("❌ This Book ID already exists. Please re-enter....")
            new_id = input("Enter the Book ID: ")
            return valid_id(new_id)

    return Id

def valid_member_id(Id):
    with open(path + "member.txt", "r") as fp:
        mData = fp.read().strip().split("\n")
    for member in mData:
        if member.strip() == "":
            continue
        member_id = member.split(", ")[0]
        if Id == member_id:
            print("❌ This Member ID already exists. Please re-enter....")
            new_id = input("Enter the Member ID: ")
            return valid_member_id(new_id)

    return Id
