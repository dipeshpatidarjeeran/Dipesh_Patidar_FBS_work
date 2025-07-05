# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
    # d. Constructor (Support both parameterized and parameterless)
    # e. Destructor
    # f. ShowProduct

class Product:
    def __init__(self,pid,pname,quantity,price=200):
        self.pname = pname
        self.pid = pid
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("Product Id:",self.pid)
        print("Product Name:",self.pname)
        print("Quantity:",self.quantity)
        print("Price:",self.price)
        print("_"*30)

    def __del__(self):
        print("Destructor is called.")

p1 = Product(101,"book",2)
p2 = Product(102,'shoes',5,1500)
p1.showProduct()
p2.showProduct()
