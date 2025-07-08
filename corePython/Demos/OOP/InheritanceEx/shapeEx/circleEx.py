##### hierarchical inheritance 
from shape import Shape

class Circle(Shape):
    def __init__(self, Id, area, radius):
        super().__init__(Id, area)
        self.r = radius

    def display(self):
        super().display()
        print("Radius:",self.r)

c1 = Circle('c21',154,7)
c1.display()