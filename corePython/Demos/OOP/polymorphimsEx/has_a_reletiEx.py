class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.add = address

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.add)
        print("_"*25)

p1 = Person('dipesh', 24, 'MP')
p2 = Person('Ram', 25, 'Pune')
p3 = Person('raj', 21, 'Pune')


class Car:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def show(self):
        print("Name:",self.name)
        print("Model:",self.model)
        print("Price:",self.price)
        print("_"*25)

c1 = Car("BMW",'X6',5000000)

        
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
       

    def display(self):
        print("Name:",self.name)
        print("Color:",self.color)
        print("_"*25)

a1 = Animal('Dog', 'black')

# list of objects
# mentain has a reletionship
objs = [p1,p2,p3,a1,c1]

for obj in objs:
    if hasattr(obj,'display'):
        obj.display()