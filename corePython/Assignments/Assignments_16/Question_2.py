# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
#     e. Constructor (Support both parameterized and parameterless)
#     f. Destructor
#     g. ShowProduct
#     h. Add static member discount.
#     i. Provide methods for applying discount on price of product.

class Product:
    discount = 30
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

    def applyDiscount(self):
        dis_amount = (self.price * Product.discount)/100
        self.price = dis_amount
        print(f"Discount of {Product.discount}% applied. New price: {self.price}")

p1 = Product(101,"book",2)
p2 = Product(102,'shoes',5,1500)
p1.showProduct()
p2.showProduct()

p2.applyDiscount()
