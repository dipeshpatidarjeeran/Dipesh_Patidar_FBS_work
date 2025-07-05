# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
    # a. Constructor (Support both parameterized and parameterless)
    # b. Destructor
    # c. ShowBook
class Book:
    def __init__(self,bid,bname,author,price=300):
        self.bname = bname
        self.bid = bid
        self.price = price
        self.author = author

    def showBook(self):
        print("Book Name:",self.bname)
        print("Book Id:",self.bid)
        print("Author:",self.author)
        print("Price:",self.price)
        print("_"*30)

    def __del__(self):
        print("Destructor is called.")


b1 = Book(101,'brave new world',"author_1")
b2 = Book(102,'Geeta','author_name2',500)
b1.showBook()
b2.showBook()