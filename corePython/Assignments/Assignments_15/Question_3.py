# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
    # g. Constructor (Support both parameterized and parameterless)
    # h. Destructor
    # i. Showshirt
class Shirt:
    def __init__(self,sid,sname,size,type='formal',price=300):
        self.sname = sname
        self.sid = sid
        self.price = price
        self.type = type
        self.size = size

    def showShirt(self):
        print("shirt Id:",self.sid)
        print("short Name:",self.sname)
        print("short tpye:",self.type)
        print("short size:",self.size)
        print("Price:",self.price)
        print("_"*30)

    def __del__(self):
        print("Destructor is called.")


s1 = Shirt(101,'plain shirt',"small")
s2 = Shirt(102,'printed shirt','large',"casual",500)
s1.showShirt()
s2.showShirt()