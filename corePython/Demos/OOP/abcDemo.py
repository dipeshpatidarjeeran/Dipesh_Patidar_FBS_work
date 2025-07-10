from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def stop(self):
        pass

class Bike(Vehicle):
    def __init__(self, name, type, price, color):
        self.name = name
        self.type = type
        self.price = price
        self.color = color

    def stop(self):
        print("Bike stooped.")

b1 = Bike('shine', 'BS6', 115000, 'black')
b1.stop()

        