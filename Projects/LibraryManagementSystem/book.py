class Book:
    def __init__(self, Id, title, author, copies, bcount, status):
        self.bid = Id
        self.title = title
        self.author = author
        self.copies = copies
        self.bcount = bcount
        self.bstatus = status

    def __str__(self):
        return f'{self.bid}, {self.title}, {self.author}, {self.copies}, {self.bcount}, {self.bstatus}'