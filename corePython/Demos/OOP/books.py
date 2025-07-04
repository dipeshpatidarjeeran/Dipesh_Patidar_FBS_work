class Book:
    def setData(self,name,page,price):
        self.nm = name
        self.page_no = page
        self.price = price

    def getData(self):
        print("Book Name:",self.nm)
        print("Number of pages:",self.page_no)
        print("Price:",self.price)
        print("_"*30)

b1 = Book()
b2 = Book()
b1.setData('Geeta',250,500)
b2.setData('brave new world',100,300)
b1.getData()
b2.getData()