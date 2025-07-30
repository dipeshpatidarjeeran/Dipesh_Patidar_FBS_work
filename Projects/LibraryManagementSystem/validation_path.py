from colorama import Fore, Style
path = "C:/Users/HP/Desktop/FBS/Projects/LibraryManagementSystem/data/"


def valid_id(Id):
    with open(path + "bookDetails.txt", "r") as fp:
        bData = fp.read().strip().split("\n")
    for book in bData:
        if book.strip() == "":
            continue
        book_id = book.split(", ")[0]
        if Id == book_id:
            print(Fore.RED + Style.BRIGHT + "❌ This Book ID already exists. Please re-enter...." + Style.RESET_ALL)
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
            print(Fore.RED + Style.BRIGHT + "❌ This Member ID already exists. Please re-enter...." + Style.RESET_ALL)
            new_id = input("Enter the Member ID: ")
            return valid_member_id(new_id)

    return Id


def get_valid_phone(phone):
    if phone.isdigit() and len(phone) == 10 and phone[0] not in ['0', '1']:
        return phone
    else:
        print(Fore.RED + Style.BRIGHT + "❌ Invalid phone number. Please enter a valid 10-digit number." + Style.RESET_ALL)
        phone = input("Enter the Phone Number: ")
        return get_valid_phone(phone)


def valid_name(name):
    if name.isalpha() and len(name.strip()) >= 2:
        return name.title()
    else:
        print(Fore.RED + Style.BRIGHT + "❌ Invalid name. Only alphabets allowed and must be at least 2 characters." + Style.RESET_ALL)
        name = input("Enter your name: ")
        return valid_name(name)
