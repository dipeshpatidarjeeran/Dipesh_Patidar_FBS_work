from colorama import Fore, Style
from bookMangement import BookManagement
from memberMangement import MemberManagement
from issueMangement import IssueMangement
from paymentManagement import PaymentMangement

bm = BookManagement()
m = MemberManagement()
im = IssueMangement()
pm = PaymentMangement()

class Librarian:
    def __init__(self):
        ch = 0 
        while(ch != '13'):
            print(Fore.YELLOW + Style.BRIGHT +
            """📋 Please select choice
            1. Add Book
            2. Search Book
            3. View All Books
            4. Remove Book
            5. Register Member
            6. View All Members
            7. Issue Book
            8. Return Book
            9. View Issued Books
            10. Remove Member
            11. Pay Fine
            12. Show Transactions
            13. logout""" + Style.RESET_ALL)
            
            ch = input("Enter the choice:-")

            if(ch == '1'):
                bm.addBook()

            elif(ch == '2'):
                bm.GetBook()

            elif(ch == '3'):
                bm.showAllBook()

            elif(ch == '4'):
                bm.deleteBook()

            elif(ch == '5'):
                m.addMember()

            elif(ch == '6'):
                m.showAllMember()
            
            elif(ch == '7'):
                im.issue_book()
            
            elif(ch == '8'):
                im.return_book()

            elif(ch == '9'):
                im.show_issued_book()

            elif(ch == '10'):
                m.deleteMember()

            elif(ch == '11'):
                pm.pay_fine()

            elif(ch == '12'):
                pm.show_all_transaction()

            elif(ch == '13'):
                print(Fore.GREEN + Style.BRIGHT + "🔓 Logout successful." + Style.RESET_ALL)

            else:
                print(Fore.RED + Style.BRIGHT + "❌ Invalid choice. Please try again." + Style.RESET_ALL)
