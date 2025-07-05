###Destructor:
#1. special method called autometically when life cycle of object is completed.
    #or  when we are deleting the object.
#2. basically used for closing below resoures.
    #- files
    #- network ports
    #- database connections
#3. use __del__ as name of a destructor

class Person:
    def __init__(self, name, address, age):
        self.nm = name
        self.add = address
        self.age = age

    def __del__(self):
        print("Destructor is called.")

    def showData(self):
        print("Name:",self.nm)
        print("address:",self.add)
        print("age:",self.age)
        print("_"*25)

p1 = Person("dipesh", "Pune", 24)
p2 = Person("ram", "Pune", 22)
p3 = Person("vinod", "MP", 32)

p1.showData()
p2.showData()
p3.showData()