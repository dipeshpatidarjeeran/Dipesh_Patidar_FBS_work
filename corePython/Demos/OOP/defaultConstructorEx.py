class Animal:
    def __init__(self, name="Dog",type="Pet",color="Black",gender="Male"):
        self.name = name
        self.type = type
        self.color = color
        self.gender = gender
    
    def getData(self):
        return f'Name:{self.name}\ntype:{self.type}\nColor:{self.color}\nGender:{self.gender}'
    
cat = Animal("cat","pet","black","Female")
print(cat.getData())
print("_"*25)
a1 = Animal()
print(a1.getData())