class Vehicle:
    def setData(self,name,model,colour):
        self.vehi_name = name
        self.model = model
        self.col = colour

    def getData(self):
        print("Name:", self.vehi_name)
        print("Model:", self.model)
        print("Colour:", self.col)
        print("#"*20)

obj1 = Vehicle()
obj2 = Vehicle()
obj3 = Vehicle()

obj1.setData("BMW",'BMW-21',"red")
obj2.setData("john deere",'5150',"green")
obj3.setData("mahindra",'735',"red")

obj1.getData()
obj2.getData()
obj3.getData()
