# 
class Animal:
    def sound(self):
        print("sound of animal")

class Cat(Animal):
    def sound(self):
        print("Meow Meow!!!")

c1 = Cat()
c1.sound()