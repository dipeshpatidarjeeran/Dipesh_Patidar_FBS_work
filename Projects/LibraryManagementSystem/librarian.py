from bookMangement import BookManagement
from memberMangement import MemberManagement
from issueMangement import IssueMangement
bm = BookManagement()
m = MemberManagement()
im = IssueMangement()

class Librarian:
    def __init__(self):
        ch = 0 
        while(ch != '10'):
            print("""Please select choice
                1. Add Book
                2. Search Book
                3. View All Books
                4. Remove Book
                5. Register Member
                6. View All Members
                7. Issue Book
                8. Return Book
                9. View Issued Books
                10. logout""")
            
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
                pass

            elif(ch == '9'):
                pass

            elif(ch == '10'):
                print("logout successful...")

            else:
                print("Invalid choice...Please try again")
