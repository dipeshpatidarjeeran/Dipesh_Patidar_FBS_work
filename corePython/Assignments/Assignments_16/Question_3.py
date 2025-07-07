# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
#     j. Constructor (Support both parameterized and parameterless)
#     k. Destructor
#     l. ShowBook
#     m. For each size of shirt price should change by 10%.
#     (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
#     xlarge=1300) Use static concept.

class Shirt:
    small = 1.0
    medium = 1.1
    large = 1.2
    xlarge = 1.3
    def __init__(self,sid,sname,size,type='formal',price=300):
        self.sname = sname
        self.sid = sid
        self.price = price
        self.type = type
        self.size = size

    def showShirt(self):
        if self.size == "small":
            self.price *= Shirt.small

        elif self.size == "medium":
            self.price *= Shirt.medium

        elif self.size == "large":
            self.price *= Shirt.large

        elif self.size == "xlarge":
            self.price *= Shirt.xlarge
        
        print("shirt Id:",self.sid)
        print("short Name:",self.sname)
        print("short tpye:",self.type)
        print("short size:",self.size)
        print("Price:",self.price)
        print("_"*30)

    def __del__(self):
        print("Destructor is called.")


s1 = Shirt(101,'plain shirt',"xlarge")
s2 = Shirt(102,'printed shirt','large',"casual",500)
s1.showShirt()
s2.showShirt()